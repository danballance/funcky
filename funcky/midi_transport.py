from rtmidi import MidiIn, MidiOut
from rtmidi.midiconstants import SONG_START, SONG_STOP, SONG_CONTINUE, TIMING_CLOCK

from funcky.song_base import SongProtocol


class MidiTransport:
    def __init__(
        self,
        input_port_name: str,
        output_port_name: str,
        song: SongProtocol
    ) -> None:
        self._input_port_name: str = input_port_name
        self._output_port_name: str = output_port_name
        self._song: SongProtocol = song
        self._midi_in = MidiIn()
        self._midi_out = MidiOut()

    def play(self) -> None:
        self._open_ports()
        while True:
            msg = self._midi_in.get_message()
            if msg:
                message, _ = msg
                self._handle_message(message)

    def _open_ports(self):
        available_inputs = self._midi_in.get_ports()
        available_outputs = self._midi_out.get_ports()
        if self._input_port_name in available_inputs:
            self._midi_in.open_port(available_inputs.index(self._input_port_name))
        else:
            raise ValueError(f"Input port {self._input_port_name} not found.")
        if self._output_port_name in available_outputs:
            self._midi_out.open_port(available_outputs.index(self._output_port_name))
        else:
            raise ValueError(f"Output port {self._output_port_name} not found.")
        # Ensure we are not filtering any MIDI messages, including clock messages
        self._midi_in.ignore_types(sysex=False, timing=False)
        print(f"Listening for MIDI on: {self._input_port_name}")
        print(f"Sending MIDI on: {self._output_port_name}")

    def _handle_message(self, msg: list[int]) -> None:
        status_byte = msg[0]
        if status_byte == SONG_START:
            print("Received START")
            self._song.song_start()

        elif status_byte == SONG_STOP:
            print("Received STOP")
            self._song.song_stop()

        elif status_byte == SONG_CONTINUE:
            print("Received CONTINUE")
            self._song.song_continue()

        elif status_byte == TIMING_CLOCK:
            print("Received TIMING CLOCK")
            for msg in self._song.tick():
                print(f"{msg=}")
                if msg:
                    self._midi_out.send_message(msg.to_wire())

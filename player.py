from funcky.midi_transport import MidiTransport
from tracks.hello_world.song import song

if __name__ == '__main__':
    transport = MidiTransport(
        input_port_name='IAC Driver Bus 1',
        output_port_name='IAC Driver Bus 1',
        song=song
    )
    transport.play()

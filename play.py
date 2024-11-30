from funcky.midi_transport import MidiTransport
from funcky.mono_note_sequence import MonoNoteSequence
from songs.hello_world import HelloWorld

if __name__ == '__main__':
    song = HelloWorld(
        note_sequence=MonoNoteSequence()
    )
    transport = MidiTransport(
        input_port_name='IAC Driver Bus 1',
        output_port_name='IAC Driver Bus 1',
        song=song
    )
    transport.play()

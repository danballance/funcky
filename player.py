import signal
import sys

from funcky.utils.debug import handle_sigint, excepthook
from funcky.midi_transport import MidiTransport
from tracks.hello_world.song import song

# Set up the SIGINT handler
signal.signal(signal.SIGINT, handle_sigint)
# Set up the global unhandled exception hook
sys.excepthook = excepthook


if __name__ == '__main__':
    transport = MidiTransport(
        input_port_name='IAC Driver Bus 1',
        output_port_name='IAC Driver Bus 1',
        song=song
    )
    transport.play()

from dataclasses import dataclass
from enum import StrEnum, IntEnum, Enum
from typing import Literal

TICKS_PER_BAR = 96

Step = Literal[1, 2, 4, 8, 16, 32]
VALID_STEPS = tuple([1, 2, 4, 8, 16, 32])


class Tone(IntEnum):
    C  = 0
    D  = 2
    E  = 4
    F  = 5
    G  = 7
    A  = 9
    B  = 11


Sharp = Literal[1]
Natural = Literal[0]
Flat = Literal[-1]
Accidental = Literal[Sharp, Natural, Flat]
Octave = Literal[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


@dataclass
class Pitch:
    tone: Tone
    octave: Octave
    accidental: Accidental

    def to_midi(self) -> int:
        """
        Convert the Pitch to its corresponding MIDI note number.
        MIDI Note Number = 12 * (octave + 1) + tone_value + accidental
        Returns:
            int: The MIDI note number.
        """
        midi_number = 12 * (self.octave + 1) + self.tone.value + self.accidental
        return midi_number


class Mode(Enum):
    Major = [0, 2, 4, 5, 7, 9, 11, 12]
    Minor = [0, 2, 3, 5, 7, 8, 10, 12]
    HarmonicMinor = [0, 2, 3, 5, 7, 8, 11, 12]
    MelodicMinor = [0, 2, 3, 5, 7, 9, 11, 12]


class DebugSequenceKey(StrEnum):
    EVENT = "event"
    NOTE = "note"

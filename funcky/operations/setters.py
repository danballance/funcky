"""
Setters can only insert new notes into empty ticks.
They are mostly used as an initiating operation to begin a part.
"""
from funcky.sequences import NoteSequence
from funcky.types import Note

pattern_1_8 = [0, 12, 24, 36, 48, 60, 72, 84]
pattern_1_4 = [0, 24, 48, 72]
pattern_1_4_offset_12 = [12, 36, 60, 84]

def repetition(seq: NoteSequence) -> NoteSequence:
    total_iterations = 96
    for i in range(total_iterations):
        if seq[i] is None and i in pattern_1_8:
            seq[i] = Note(note=60, duration=6, velocity=64)  # Note on, middle C, velocity 64
    return seq

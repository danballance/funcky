from funcky.decorators import Repetition, Scale
from funcky.named_constants import Key
from funcky.rhythm import steps_8
from funcky.sequences.note_sequence import NoteSequence


@Scale(key=Key.Cm)
@Repetition(steps=steps_8)
def track_one(seq: NoteSequence) -> NoteSequence:
    return seq

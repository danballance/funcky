from funcky.operations.decorators import RepetitionDecorator, ScaleDecorator
from funcky.sequences.note_sequence import NoteSequence


@ScaleDecorator
@RepetitionDecorator
def track_one(seq: NoteSequence) -> NoteSequence:
    return seq

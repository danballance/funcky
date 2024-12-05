from funcky.decorators.repetition import Repetition
from funcky.decorators.tune import Tune

from funcky.named_constants import Pitch, Tone, Mode
from funcky.rhythm import steps_8
from funcky.scales import scale_generator
from funcky.sequences.note_sequence import NoteSequence


@Tune(
    scale_generator=scale_generator(
        root=Pitch(tone=Tone.C, octave=4, accidental=0),
        mode=Mode.Major,
        notes=lambda: [1, 2, 3, 4, 5, 6, 7, 8],
    )
)
@Repetition(steps=steps_8)
def track_one(seq: NoteSequence) -> NoteSequence:
    return seq

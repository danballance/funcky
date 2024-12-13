from funcky.decorators.accent import Accent
from funcky.decorators.repetition import Repetition
from funcky.decorators.transpose import Transpose
from funcky.decorators.tune import Tune

from funcky.named_constants import Pitch, Tone, Mode
from funcky.rhythm import steps_16
from funcky.scales import scale_generator
from funcky.sequences.note_mono_sequence import NoteMonoSequence


@Accent(
    cycle_length=1,
    accent_pattern=[50, 0, 0, 25, 50, 0, 25, 0]
)
@Transpose(
    cycle_length=8,
    transposition_pattern=[0, 0, 2, 1]
)
@Tune(
    scale_generator=scale_generator(
        root=Pitch(tone=Tone.C, octave=3, accidental=0),
        mode=Mode.Minor,
        notes=lambda: [1, 3, 4, 5],
    )
)
@Repetition(steps=steps_16)
def track_one(seq: NoteMonoSequence) -> NoteMonoSequence:
    return seq

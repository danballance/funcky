from funcky.named_constants import Tone, Mode, Pitch
from funcky.scales import scale_generator


def test_default_c_major_scale():
    generator = scale_generator(
        root=Pitch(tone=Tone.C, octave=4, accidental=0),
        mode=Mode.Major,
        notes=lambda: [1, 2, 3, 4, 5, 6, 7, 8],
    )
    # 2 cycles proves generator continues forever
    midi_notes = [60, 62, 64, 65, 67, 69, 71, 72, 60, 62, 64, 65, 67, 69, 71, 72]
    for midi_note in midi_notes:
        assert next(generator) == midi_note

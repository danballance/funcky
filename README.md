# Funcky

Example syntax looks like this 
([link](https://github.com/danballance/funcky/blob/main/tracks/hello_world/tracks.py#L12-L29)):
```python
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
@Repetition(steps=steps_8)
def track_one(seq: NoteSequence) -> NoteSequence:
    return seq
```

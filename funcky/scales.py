from collections.abc import Iterable, Generator
from itertools import cycle
from typing import Callable

from funcky.named_constants import Mode, Pitch


def scale_generator(
    root: Pitch,
    mode: Mode,
    notes: Callable[..., Iterable[int]] | None = None
) -> Generator[int]:
    root_note_midi = root.to_midi()
    midi_scale = [root_note_midi + interval for interval in mode.value]
    for note in cycle(notes()):
        # we don't want to make users call first note in a scale 0, so adjust here
        yield midi_scale[note - 1]

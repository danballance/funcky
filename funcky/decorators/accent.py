from itertools import cycle
from typing import Generator

from funcky.decorators.base_decorator import BaseDecorator
from funcky.sequences.note_mono_sequence import NoteMonoSequence


class Accent(BaseDecorator):
    _accent_generator: Generator[int]

    def __init__(
        self,
        cycle_length: int,
        accent_pattern: list[int],
    ):
        self._accent_generator = self._make_accent_generator(
            cycle_length=cycle_length,
            accent_pattern=accent_pattern,
        )

    def _decorate(self, seq: NoteMonoSequence, i: int) -> NoteMonoSequence:
        if seq[i] is not None:
            seq[i].velocity += self._accent_generator.__next__()
        return seq

    @staticmethod
    def _make_accent_generator(
        cycle_length: int,
        accent_pattern: list[int],
    ) -> Generator[int]:
        for accent in cycle(accent_pattern):
            for _ in range(cycle_length):
                yield accent

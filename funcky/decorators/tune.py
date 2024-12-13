from typing import Generator

from funcky.decorators.base_decorator import BaseDecorator
from funcky.sequences.note_mono_sequence import NoteMonoSequence


class Tune(BaseDecorator):
    _scale_generator: Generator[int]

    def __init__(
        self,
        scale_generator: Generator[int]
    ):
        self._scale_generator = scale_generator

    def _decorate(self, seq: NoteMonoSequence, i: int) -> NoteMonoSequence:
        if seq[i] is not None:
            seq[i].note = self._scale_generator.__next__()
        return seq

import os
from abc import ABC, abstractmethod
from collections import defaultdict
from functools import wraps
from typing import Iterable

from funcky.sequences.note_sequence import SequenceOperation, NoteSequence

DEBUG = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")


class BaseDecorator(ABC):
    _debug_data: dict[str, list[NoteSequence]] = defaultdict(list)

    @classmethod
    def get_debug_data(cls) -> dict[str, list[NoteSequence]]:
        return cls._debug_data

    def __call__(self, func: SequenceOperation) -> SequenceOperation:
        @wraps(func)
        def wrapper(*args, **kwargs):
            seq = func(*args, **kwargs)
            for i in self._indexes(seq):
                seq = self._decorate(seq, i)
            if DEBUG:
                self._debug_data[self.__class__.__name__].append(seq)
            return seq
        return wrapper

    def _indexes(self, seq: NoteSequence) -> Iterable[int]:
        """
        Override this method to provide a non-incremental means of
        iterating over the note sequence.
        """
        return list(range(len(seq)))

    @abstractmethod
    def _decorate(self, seq: NoteSequence, i: int) -> NoteSequence:
        """
        Implement this method to manipulate the note sequence.
        """
        pass

from abc import ABC, abstractmethod
from functools import wraps
from typing import Iterable

from funcky.sequences.note_sequence import SequenceOperation, NoteSequence


class BaseDecorator(ABC):
    def __call__(self, func: SequenceOperation) -> SequenceOperation:
        @wraps(func)
        def wrapper(*args, **kwargs):
            seq = func(*args, **kwargs)
            for i in self._indexes(seq):
                seq = self._decorate(seq, i)
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

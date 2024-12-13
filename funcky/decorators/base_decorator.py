import os
from abc import ABC, abstractmethod
from functools import wraps
from typing import Iterable

from funcky.sequences.note_mono_sequence import SequenceMonoOperation, NoteMonoSequence
from funcky.utils.debug_store import DebugStore

DEBUG = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")


class BaseDecorator(ABC):
    _func_name: str

    def __call__(self, func: SequenceMonoOperation) -> SequenceMonoOperation:
        self._func_name = func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            seq = func(*args, **kwargs)
            for i in self._indexes(seq):
                seq = self._decorate(seq, i)
            if DEBUG:
                DebugStore.add_note_sequence(
                    track_name=self._func_name,
                    decorator_name=self.__class__.__name__,
                    note_sequence=seq.copy(),
                )
            return seq
        return wrapper

    def _indexes(self, seq: NoteMonoSequence) -> Iterable[int]:
        """
        Override this method to provide a non-incremental means of
        iterating over the note sequence.
        """
        return list(range(len(seq)))

    @abstractmethod
    def _decorate(self, seq: NoteMonoSequence, i: int) -> NoteMonoSequence:
        """
        Implement this method to manipulate the note sequence.
        """
        pass

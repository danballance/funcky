from abc import ABC, abstractmethod
from typing import Generator, Protocol

from funcky.sequences import EventSequence, SequenceOperation
from funcky.mono_note_sequence import MonoNoteSequence
from funcky.types import Event


class SongProtocol(Protocol):
    def tick(self) -> Generator[EventSequence, None, None]:
        pass

    def song_start(self) -> None:
        pass

    def song_continue(self) -> None:
        pass

    def song_stop(self) -> None:
        pass


class SongBase(ABC, SongProtocol):
    _clock_pulses: int
    _note_sequence: MonoNoteSequence

    def __init__(self, note_sequence: MonoNoteSequence):
        self._clock_pulses = -1
        self._note_sequence = note_sequence

    @property
    @abstractmethod
    def _operations(self) -> list[SequenceOperation]:
        raise NotImplemented

    @property
    def _current_tick(self) -> int:
        return self._clock_pulses % 96

    def tick(self) -> Generator[Event, None, None]:
        self._clock_pulses += 1
        print(f"clock is now {self._current_tick}")
        self._note_sequence.progress(
            self._current_tick,
            self._operations,
        )
        yield self._note_sequence.current_events()[self._current_tick]

    def song_start(self) -> None:
        pass

    def song_continue(self) -> None:
        pass

    def song_stop(self) -> None:
        pass

from abc import ABC
from typing import Generator, Protocol

from funcky.parts.mono_part import MonoPart
from funcky.dtos import Event
from funcky.parts.part import Part


class SongProtocol(Protocol):
    def tick(self) -> Generator[Event, None, None]:
        pass

    def song_start(self) -> None:
        pass

    def song_continue(self) -> None:
        pass

    def song_stop(self) -> None:
        pass


class SongBase(ABC, SongProtocol):
    _clock_pulses: int
    _note_sequence: MonoPart

    def __init__(self, tracks: list[Part]):
        self._clock_pulses = -1
        self._tracks = tracks

    @property
    def _current_tick(self) -> int:
        return self._clock_pulses % 96

    def tick(self) -> Generator[Event, None, None]:
        self._clock_pulses += 1
        print(f"clock is now {self._current_tick}")
        # @TODO temporary - refactor for multiple tracks
        self._tracks[0].progress(
            self._current_tick,
        )
        yield self._tracks[0].current_events()[self._current_tick]
        # @TODO temporary - refactor for multiple tracks

    def song_start(self) -> None:
        pass

    def song_continue(self) -> None:
        pass

    def song_stop(self) -> None:
        pass

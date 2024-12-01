from abc import ABC, abstractmethod

from funcky.sequences.event_sequence import EventSequence


class Part(ABC):

    @abstractmethod
    def progress(self, current_tick: int) -> None:
        raise NotImplemented

    @abstractmethod
    def current_events(self) -> EventSequence:
        raise NotImplemented

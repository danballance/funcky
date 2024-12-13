from abc import ABC, abstractmethod

from funcky.sequences.event_mono_sequence import EventMonoSequence


class Part(ABC):

    @abstractmethod
    def progress(self, current_tick: int) -> None:
        raise NotImplemented

    @abstractmethod
    def current_events(self) -> EventMonoSequence:
        raise NotImplemented

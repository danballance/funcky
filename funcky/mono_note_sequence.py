from typing import Iterable, Type

from funcky.sequences import GenericSequence, NoteSequence, SequenceOperation, EventSequence
from funcky.types import Note, Event

MonoNoteBar = list[Note | None]

class MonoNoteSequence:
    """
    Every NoteSequence consists of 3 x 96 ticks bars
     - bar 0 - this is the previous bar that has finished playing (past)
     - bar 1 - this is the current bar this is being played (present)
     - bar 2 - this is the next bar that will play next (future)

    As the track plays, we move 1 tick at a time through bar1 from 0 to 95
    On completing bar1 (i.e. tick 95 is complete):
     - bar0 is deleted
     - bar1 becomes bar0
     - bar2 becomes bar1
     - a new bar2 is generated
    """

    ticks_per_bar: int
    note_bars: dict[str, NoteSequence]
    event_bars: dict[str, EventSequence]

    def __init__(self, ticks_per_bar: int = 96):
        """
        Default ticks per bar is the standard midi division of 96 clock ticks
        """
        self.ticks_per_bar = ticks_per_bar
        self.note_bars = {
            "last": NoteSequence(size=ticks_per_bar),
            "current": NoteSequence(size=ticks_per_bar),
            "next": NoteSequence(size=ticks_per_bar),
        }
        self.event_bars = {
            "last": EventSequence(size=ticks_per_bar),
            "current": EventSequence(size=ticks_per_bar),
            "next": EventSequence(size=ticks_per_bar),
        }

    def progress(self, current_tick: int, operations: list[SequenceOperation]) -> None:
        if current_tick == 0:
            print("Progressing bars")
            self.note_bars = self._progress_bars(self.note_bars, NoteSequence)
            self.event_bars = self._progress_bars(self.event_bars, EventSequence)
            print("Next notes loaded to current:")
            print(self.note_bars["current"])
            print("Next events loaded to current:")
            print(self.event_bars["current"])
            print("Determining current bar")
            for operation in operations:
                print(f"Running operation: {operation.__name__}")
                self.note_bars["current"] = operation(self.note_bars["current"])
            self.event_bars["current"], self.event_bars["next"] = self.note_bars["current"].update_events(
                self.event_bars["current"],
                self.event_bars["next"]
            )
            print("Current notes:")
            print(self.note_bars["current"])
            print("Current events:")
            print(self.event_bars["current"])

    def _progress_bars(
        self,
        bars: dict[str, NoteSequence | EventSequence],
        sequence_type: Type[NoteSequence | EventSequence]
    ) -> dict[str, NoteSequence | EventSequence]:
        bars["last"] = bars["current"]
        bars["current"] = bars["next"]
        bars["next"] = sequence_type(size=self.ticks_per_bar)
        return bars

    def current_events(self) -> EventSequence:
        return self.event_bars["current"]

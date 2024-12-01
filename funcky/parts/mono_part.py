from typing import Type

from funcky.parts.part import Part
from funcky.dtos import Note
from funcky.sequences.event_sequence import EventSequence
from funcky.sequences.note_sequence import NoteSequence, SequenceOperation

MonoNoteBar = list[Note | None]

class MonoPart(Part):
    """
    Every NoteSequence consists of 3 x 96 ticks bars
     - last bar - this is the previous bar that has finished playing (past)
     - current bar - this is the current bar this is being played (present)
     - next bar - this is the next bar that will play next (future)

    As the track plays, we move 1 tick at a time through current from 0 to ticks_per_bar-1 (default 95)
    On completing current bar (i.e. tick 95 is complete):
     - last bar is deleted
     - current bar becomes last bar
     - next becomes current bar
     - a new next bar is created
    """

    ticks_per_bar: int
    _generator: SequenceOperation
    note_bars: dict[str, NoteSequence]
    event_bars: dict[str, EventSequence]

    def __init__(self, generator: SequenceOperation, ticks_per_bar: int = 96):
        """
        Default ticks per bar is the standard midi division of 96 clock ticks
        """
        self._generator = generator
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

    def progress(self, current_tick: int) -> None:
        if current_tick == 0:
            print("Progressing bars")
            self.note_bars = self._progress_bars(self.note_bars, NoteSequence)
            self.event_bars = self._progress_bars(self.event_bars, EventSequence)
            print("Running current bar through the track's generator")
            self.note_bars["current"] = self._generator(self.note_bars["current"])
            self.event_bars["current"], self.event_bars["next"] = self.note_bars["current"].update_events(
                self.event_bars["current"],
                self.event_bars["next"]
            )

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

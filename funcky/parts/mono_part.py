from typing import Type

from funcky.parts.part import Part
from funcky.dtos import Note
from funcky.sequences.event_poly_sequence import EventPolySequence
from funcky.sequences.note_mono_sequence import NoteMonoSequence, SequenceMonoOperation

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
    _generator: SequenceMonoOperation
    note_bars: dict[str, NoteMonoSequence]
    event_bars: dict[str, EventPolySequence]

    def __init__(self, generator: SequenceMonoOperation, ticks_per_bar: int = 96):
        """
        Default ticks per bar is the standard midi division of 96 clock ticks
        """
        self._generator = generator
        self.ticks_per_bar = ticks_per_bar
        self.note_bars = {
            "last": NoteMonoSequence(size=ticks_per_bar),
            "current": NoteMonoSequence(size=ticks_per_bar),
            "next": NoteMonoSequence(size=ticks_per_bar),
        }
        self.event_bars = {
            "last": EventPolySequence(size=ticks_per_bar),
            "current": EventPolySequence(size=ticks_per_bar),
            "next": EventPolySequence(size=ticks_per_bar),
        }

    def progress(self, current_tick: int) -> None:
        if current_tick == 0:
            print("Progressing bars")
            self.note_bars = self._progress_bars(self.note_bars, NoteMonoSequence)
            self.event_bars = self._progress_bars(self.event_bars, EventPolySequence)
            print("Running current bar through the track's generator")
            self.note_bars["current"] = self._generator(self.note_bars["current"])
            self.event_bars["current"], self.event_bars["next"] = self.note_bars["current"].update_events(
                self.event_bars["current"],
                self.event_bars["next"]
            )

    def _progress_bars(
        self,
        bars: dict[str, NoteMonoSequence | EventPolySequence],
        sequence_type: Type[NoteMonoSequence | EventPolySequence]
    ) -> dict[str, NoteMonoSequence | EventPolySequence]:
        bars["last"] = bars["current"]
        bars["current"] = bars["next"]
        bars["next"] = sequence_type(size=self.ticks_per_bar)
        return bars

    def current_events(self) -> EventPolySequence:
        return self.event_bars["current"]

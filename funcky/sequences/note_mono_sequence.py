import sys
from typing import Callable

from rtmidi.midiconstants import NOTE_ON, NOTE_OFF

from funcky.sequences.event_poly_sequence import EventPolySequence
from funcky.sequences.generic_mono_sequence import GenericMonoSequence
from funcky.dtos import Note, Event


class NoteMonoSequence(GenericMonoSequence):
    _items = list[Note | None]

    def __init__(self, size: int):
        super().__init__(size)

    def update_events(
        self,
        current_events: EventPolySequence,
        next_events: EventPolySequence
    ) -> tuple[EventPolySequence, EventPolySequence]:
        for i, note in enumerate(self._items):
            if note is not None:
                current_events[i] = Event(cmd=NOTE_ON, note=note.note, velocity=note.velocity)
                note_off_tick = i + note.duration
                if note_off_tick < self._size:
                    current_events[note_off_tick] = Event(cmd=NOTE_OFF, note=note.note, velocity=note.velocity)
                else:
                    note_off_tick = note_off_tick - self._size
                    next_events[note_off_tick] = Event(cmd=NOTE_OFF, note=note.note, velocity=note.velocity)
        return current_events, next_events


SequenceMonoOperation = Callable[[NoteMonoSequence], NoteMonoSequence]

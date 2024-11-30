from typing import Sequence, TypeVar, Generic, Callable

from rtmidi.midiconstants import NOTE_ON, NOTE_OFF

from funcky.types import Event, Note

T = TypeVar('T')


class GenericSequence(Generic[T]):
    _items = list[T | None]

    def __init__(self, size: int):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __setitem__(self, index: int, value: T) -> None:
        if self._items[index] is not None:
            raise ValueError("Cannot overwrite existing items")
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._items[index] = value

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"GenericSequence({self._items})"


class EventSequence(GenericSequence[T]):
    _items = list[Event | None]

    def __init__(self, size: int):
        super().__init__(size)


class NoteSequence(GenericSequence[T]):
    _items = list[Note | None]

    def __init__(self, size: int):
        super().__init__(size)

    def update_events(
        self,
        current_events: EventSequence,
        next_events: EventSequence
    ) -> tuple[EventSequence, EventSequence]:
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


SequenceOperation = Callable[[NoteSequence], NoteSequence]

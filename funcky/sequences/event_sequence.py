from funcky.sequences.generic_sequence import GenericSequence
from funcky.dtos import Event


class EventSequence[T](GenericSequence[T]):
    _items = list[Event | None]

    def __init__(self, size: int):
        super().__init__(size)

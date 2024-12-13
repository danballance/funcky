from funcky.dtos import Event
from funcky.sequences.generic_poly_sequence import GenericPolySequence


class EventPolySequence[T](GenericPolySequence[T]):
    _items = list[list[Event]]

    def __init__(self, size: int):
        super().__init__(size)

from funcky.sequences.generic_mono_sequence import GenericMonoSequence
from funcky.dtos import Event


class EventMonoSequence[T](GenericMonoSequence[T]):
    _items = list[Event | None]

    def __init__(self, size: int):
        super().__init__(size)

import copy


class GenericSequence[T]:
    _items = list[T | None]

    def __init__(self, size: int):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __setitem__(self, index: int, value: T) -> None:
        if self._items[index] is not None:
            old_value = self._items[index]
            raise ValueError(f"Cannot overwrite existing items: {index=} old_value={old_value} new_value={value}")
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of range {index=}")
        self._items[index] = value

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"GenericSequence({self._items})"

    def copy(self) -> "GenericSequence[T]":
        """
        Returns a deep copy of the data to ensure no references back to the original.
        """
        new_copy = GenericSequence(self._size)
        new_copy._items = copy.deepcopy(self._items)
        return new_copy

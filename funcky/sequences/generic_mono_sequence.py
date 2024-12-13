import copy


class GenericMonoSequence[T]:
    _items = list[T | None]

    def __init__(self, size: int):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index: int) -> T | None:
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

    def __delitem__(self, index: int) -> None:
        if index in self._items:
            self._items[index] = None

    def __repr__(self) -> str:
        return f"GenericSequence({self._items})"

    def copy(self) -> "GenericMonoSequence[T]":
        """
        Returns a deep copy of the data to ensure no references back to the original.
        """
        new_copy = GenericMonoSequence(self._size)
        new_copy._items = copy.deepcopy(self._items)
        return new_copy

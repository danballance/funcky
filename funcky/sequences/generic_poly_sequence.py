import copy


class GenericPolySequence[T]:
    _items = list[list[T]]

    def __init__(self, size: int):
        self._size = size
        self._items = [[] for _ in range(size)]

    def __getitem__(self, index: int) -> list[T]:
        return self._items[index]

    def __setitem__(self, index: int, value: T) -> None:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of range {index=}")
        self._items[index].append(value)

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"GenericSequence({self._items})"

    def copy(self) -> "GenericPolySequence[T]":
        """
        Returns a deep copy of the data to ensure no references back to the original.
        """
        new_copy = GenericPolySequence(self._size)
        new_copy._items = copy.deepcopy(self._items)
        return new_copy

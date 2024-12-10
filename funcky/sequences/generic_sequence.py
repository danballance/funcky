class GenericSequence[T]:
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

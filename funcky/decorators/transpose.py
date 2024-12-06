from functools import wraps
from itertools import cycle
from typing import Generator


class Transpose:
    _interval_generator: Generator[int]

    def __init__(
        self,
        cycle_length: int,
        transposition_pattern: list[int],
    ):
        self._interval_generator = self._make_interval_generator(
            cycle_length=cycle_length,
            transposition_pattern=transposition_pattern,
        )

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            seq = func(*args, **kwargs)
            for i in range(len(seq)):
                if seq[i] is not None:
                    seq[i].note += self._interval_generator.__next__()
            return seq
        return wrapper

    def _make_interval_generator(
        self,
        cycle_length: int,
        transposition_pattern: list[int],
    ) -> Generator[int]:
        for transposition in cycle(transposition_pattern):
            for _ in range(cycle_length):
                yield transposition

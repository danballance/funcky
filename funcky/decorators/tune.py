from functools import wraps
from typing import Generator


class Tune:
    _scale_generator: Generator[int]

    def __init__(
        self,
        scale_generator: Generator[int]
    ):
        self._scale_generator = scale_generator

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            seq = func(*args, **kwargs)
            for i in range(len(seq)):
                if seq[i] is not None:
                    seq[i].note = self._scale_generator.__next__()
            return seq
        return wrapper

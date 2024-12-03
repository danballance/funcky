from functools import wraps

from funcky.dtos import Note
from funcky.named_constants import Step, Key, VALID_STEPS
from funcky.rhythm import TicksFunc, steps_to_ticks
from funcky.type_guards import is_valid_midi


class Repetition:
    def __init__(
        self,
        steps: TicksFunc,
        root_note: int | None = 60,
        duration: Step | None = 16,
        velocity: int | None = 64
    ) -> None:
        self._steps = steps
        self._root_note = root_note
        self._duration_ticks = steps_to_ticks(duration)
        self._velocity = velocity
        if not is_valid_midi(root_note):
            raise TypeError(f"root_note of {root_note} is not a valid midi value 0-127")
        if duration not in VALID_STEPS:
            raise TypeError(f"duration of '{duration}' is not a valid Step")
        if not is_valid_midi(velocity):
            raise TypeError(f"velocity of {velocity} is not a valid midi value 0-127")

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            seq = func(*args, **kwargs)
            for i in self._steps():
                if seq[i] is None:
                    seq[i] = Note(
                        note=self._root_note,
                        duration=self._duration_ticks,
                        velocity=self._velocity
                    )
            return seq
        return wrapper


class Scale:
    def __init__(self, key: Key):
        self.key = key

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            seq = func(*args, **kwargs)  # Call the wrapped function first
            for i in range(len(seq)):
                if seq[i] is not None:
                    if i in [0, 12]:  # 1,2 - 8ths
                        seq[i].note = 60  # middle C
                    elif i in [24, 36]:  # 3,4 - 8ths
                        seq[i].note = 63  # middle Eb
                    elif i in [48, 60]:  # 5,6 - 8ths
                        seq[i].note = 67  # middle G
                    elif i in [72, 84]:  # 7,8 - 8ths
                        seq[i].note = 70  # middle Bb
            return seq
        return wrapper

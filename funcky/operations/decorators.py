from functools import wraps

from funcky.dtos import Note

pattern_1_8 = [0, 12, 24, 36, 48, 60, 72, 84]
pattern_1_4 = [0, 24, 48, 72]
pattern_1_4_offset_12 = [12, 36, 60, 84]


class RepetitionDecorator:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        seq = self.func(*args, **kwargs)  # Call the wrapped function first
        for i in range(len(seq)):
            if seq[i] is None and i in pattern_1_8:
                seq[i] = Note(note=60, duration=6, velocity=64)  # Note on, middle C, velocity 64
        return seq

class ScaleDecorator:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func

    def __call__(self, *args, **kwargs):
        seq = self.func(*args, **kwargs)  # Call the wrapped function first
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

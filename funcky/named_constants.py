from enum import StrEnum
from typing import Literal

TICKS_PER_BAR = 96

Step = Literal[1, 2, 4, 8, 16, 32]
VALID_STEPS = tuple([1, 2, 4, 8, 16, 32])


class Key(StrEnum):
    C = "C"
    Cm = "Cm"

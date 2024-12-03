from collections.abc import Iterable, Callable
from functools import partial

from funcky.named_constants import Step, VALID_STEPS, TICKS_PER_BAR

TicksFunc = Callable[..., Iterable[int]]

def steps(step: Step, offset: Step | None = 0) -> list[int]:
    offset = offset or 0
    if step not in VALID_STEPS:
        raise TypeError(f"step of '{step}' is not a valid Step")
    if offset not in tuple([0]) + VALID_STEPS:
        raise TypeError(f"offset of '{offset}' is not a valid Step")
    offset_ticks = int(TICKS_PER_BAR / offset) if offset > 0 else 0
    range_step = int(TICKS_PER_BAR / step)
    return list(range(0 + offset_ticks, TICKS_PER_BAR, range_step))

steps_32 = partial(steps, step=32)
steps_16 = partial(steps, step=16)
steps_8  = partial(steps, step=8)
steps_4  = partial(steps, step=4)
steps_2  = partial(steps, step=2)
steps_1  = partial(steps, step=1)


def steps_to_ticks(steps: Step) -> int:
    if steps not in VALID_STEPS:
        raise TypeError(f"steps of '{steps}' is not a valid Step")
    return int(TICKS_PER_BAR / steps)

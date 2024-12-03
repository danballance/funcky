from typing import TypeGuard


def is_valid_midi(value: int) -> TypeGuard[int]:
    return 0 <= value <= 127

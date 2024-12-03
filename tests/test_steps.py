import pytest

from funcky.named_constants import VALID_STEPS
from funcky.rhythm import steps


def test_steps_to_ticks_generation():
    assert steps(step=1, offset=0) == [0]
    assert steps(step=2, offset=0) == [0, 48]
    assert steps(step=4, offset=0) == [0, 24, 48, 72]
    assert steps(step=8, offset=0) == [0, 12, 24, 36, 48, 60, 72, 84]
    assert steps(step=16, offset=0) == [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90]


def test_steps_to_ticks_generation_with_offsets():
    assert steps(step=2, offset=0) == [0, 48]
    assert steps(step=4, offset=0) == [0, 24, 48, 72]
    assert steps(step=2, offset=0) == [0, 48]
    assert steps(step=4, offset=0) == [0, 24, 48, 72]


def test_steps_valid():
    for step in VALID_STEPS:
        expected_range_step = int(96 / step)
        expected_result = list(range(0, 96, expected_range_step))
        result = steps(step)
        assert result == expected_result, f"Failed for step={step}"


def test_steps_invalid_step():
    invalid_steps = [-1, 0, 5, 7, 9, 13, 97, 100, None, 'a']
    for step in invalid_steps:
        with pytest.raises(TypeError, match=f"step of '{step}' is not a valid Step"):
            steps(step)


def test_steps_valid_offset():
    for offset_step, offset_ticks in [(8, 12), (16, 6)]:
        result = steps(4, offset_step)
        expected_result = [0 + offset_ticks, 24 + offset_ticks, 48 + offset_ticks, 72 + offset_ticks]
        assert result == expected_result, f"Failed for offset={offset_step}"

@pytest.mark.parametrize('invalid_offset', [-1, 5, 7, 9, 13, 97, 100, 'a'])
def test_steps_invalid_offset(invalid_offset):
    with pytest.raises(TypeError, match=f"offset of '{invalid_offset}' is not a valid Step"):
        steps(8, invalid_offset)


def test_steps_type_errors():
    # Passing wrong types for 'step'
    with pytest.raises(TypeError):
        steps('invalid')
    with pytest.raises(TypeError):
        steps(None)
    # Passing wrong types for 'offset'
    with pytest.raises(TypeError):
        steps(12, 'invalid')
    with pytest.raises(TypeError):
        steps(12, None)

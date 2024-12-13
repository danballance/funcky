from collections.abc import Iterable

from funcky.decorators.base_decorator import BaseDecorator
from funcky.dtos import Note
from funcky.named_constants import Step, VALID_STEPS
from funcky.rhythm import TicksFunc, steps_to_ticks
from funcky.sequences.note_mono_sequence import NoteMonoSequence
from funcky.type_guards import is_valid_midi


class Repetition(BaseDecorator):
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

    def _indexes(self, seq: NoteMonoSequence) -> Iterable[int]:
        return self._steps()

    def _decorate(self, seq: NoteMonoSequence, i: int) -> NoteMonoSequence:
        if seq[i] is None:
            seq[i] = Note(
                note=self._root_note,
                duration=self._duration_ticks,
                velocity=self._velocity
            )
        return seq

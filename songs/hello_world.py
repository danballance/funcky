from typing import Callable

from funcky.sequences import NoteSequence
from funcky.operations.setters import repetition
from funcky.operations.mutators import scale
from funcky.song_base import SongBase


class HelloWorld(SongBase):

    @property
    def _operations(self) -> list[Callable[[NoteSequence], NoteSequence]]:
        return [
            repetition,
            scale
        ]

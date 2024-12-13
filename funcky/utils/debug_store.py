from collections import defaultdict
from threading import Lock
from typing import Union

from funcky.named_constants import DebugSequenceKey
from funcky.sequences.event_mono_sequence import EventMonoSequence
from funcky.sequences.note_mono_sequence import NoteMonoSequence


class DebugStore:
    """
    Singleton class to store debug data in the following format:

    dict[str, dict[DebugSequenceKey, dict[str, list[NoteSequence | EventSequence]]]]
    """
    _data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    _lock = Lock()

    def __new__(cls):
        raise RuntimeError("Instances of DebugStore cannot be created. Use class methods instead.")

    @classmethod
    def add_event_sequence(
        cls,
        track_name: str,
        decorator_name: str,
        event_sequence: EventMonoSequence
    ):
        """Add an EventSequence to the specified track."""
        with cls._lock:
            cls._data[track_name][DebugSequenceKey.EVENT][decorator_name].append(event_sequence)

    @classmethod
    def add_note_sequence(
        cls,
        track_name: str,
        decorator_name: str,
        note_sequence: NoteMonoSequence
    ):
        """Add a NoteSequence to the specified track."""
        with cls._lock:
            cls._data[track_name][DebugSequenceKey.NOTE][decorator_name].append(note_sequence)

    @classmethod
    def get_event_sequences_by_track(
        cls,
        track_name: str
    ) -> list[EventMonoSequence]:
        """Retrieve all EventSequences for the specified track."""
        with cls._lock:
            return cls._data.get(track_name, {}).get(DebugSequenceKey.EVENT, [])

    @classmethod
    def get_note_sequences_by_track(
        cls,
        track_name: str
    ) -> list[NoteMonoSequence]:
        """Retrieve all NoteSequences for the specified track."""
        with cls._lock:
            return cls._data.get(track_name, {}).get(DebugSequenceKey.NOTE, [])

    @classmethod
    def get_data_by_track(
        cls,
        track_name: str
    ) -> dict[DebugSequenceKey, dict[str, list[Union[NoteMonoSequence, EventMonoSequence]]]]:
        """Retrieve all NoteSequences for the specified track."""
        with cls._lock:
            return cls._data.get(track_name, {})

    @classmethod
    def get_all_data(
        cls
    ) -> dict[str, dict[DebugSequenceKey, dict[str, list[Union[NoteMonoSequence, EventMonoSequence]]]]]:
        """Return the entire debug data store."""
        with cls._lock:
            return cls._data

    @classmethod
    def clear_data(cls):
        """Clear all debug data."""
        with cls._lock:
            cls._data = {}

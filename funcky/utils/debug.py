import os
import sys
import traceback

from funcky.named_constants import DebugSequenceKey
from funcky.utils.debug_dumper import DebugDumper
from funcky.utils.debug_store import DebugStore

DEBUG = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")


def cleanup():
    """Common cleanup logic shared by all exit paths."""
    if DEBUG:
        print("Generating debug spreadsheets ...")
        all_debug_data = DebugStore.get_all_data()
        for track_name, track_data in all_debug_data.items():
            print(f"... write data for {track_name=}")
            spreadsheet_dumper = DebugDumper(
                track_name=track_name,
                data=track_data[DebugSequenceKey.NOTE]
            )
            spreadsheet_dumper.dump()
            print("...... done.")
        print("... all done.")


def handle_sigint(signum, frame):
    """Handler for SIGINT (Ctrl-C)."""
    print("Caught Ctrl-C signal!")
    cleanup()
    sys.exit(0)


def excepthook(exctype, value, tb):
    """Global hook for unhandled exceptions."""
    print("Unhandled exception occurred:", exctype, value)
    traceback.print_tb(tb)
    cleanup()
    sys.exit(1)

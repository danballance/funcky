import os
import sys
import traceback

from funcky.decorators.base_decorator import BaseDecorator
from funcky.utils.debug_dumper import DebugDumper

DEBUG = os.environ.get("DEBUG", "false").lower() in ("1", "true", "yes")


def cleanup():
    """Common cleanup logic shared by all exit paths."""
    if DEBUG:
        print("Running debug dumping logic...")
        csv_dumper = DebugDumper(data=BaseDecorator.get_debug_data())
        csv_dumper.dump()
        print("... done.")

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

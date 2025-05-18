from codecarbon import EmissionsTracker
from subprocess import call
import argparse
import sys

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <command>")
    sys.exit(1)

command = sys.argv[1:]

tracker = EmissionsTracker()

tracker.start()
try:
    call(command)
finally:
    tracker.stop()
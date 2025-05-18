from codecarbon import EmissionsTracker
from subprocess import call
import argparse

parser = argparse.ArgumentParser(description="Monitor the carbon emissions of a script.")
parser.add_argument('-e', "--exec", type=str, required=True, help="Path to the executable script.")
parser.add_argument('args', nargs=argparse.REMAINDER, help="Arguments to pass to the script.")
args = parser.parse_args()

tracker = EmissionsTracker()

tracker.start()
try:
    call([f"./{args.exec}", *args.args])
finally:
    tracker.stop()
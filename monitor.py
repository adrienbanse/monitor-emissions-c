import sys
from codecarbon import EmissionsTracker
from subprocess import call

path_to_exec = sys.argv[1]
tracker = EmissionsTracker()

tracker.start()
try:
    call(["./{}".format(path_to_exec)])
finally:
    tracker.stop()
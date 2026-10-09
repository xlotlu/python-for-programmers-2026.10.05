#!/usr/bin/env python

# Task:
# creați un executabil python ce primește ca argument
# în linie de comandă o specificație de timp
# în forma "HH:MM" (sau dacă avem timp și "HH:MM:SS")
# și
# 1) face countdown explicit sau nu
# 2) eventual rulează un payload
#    (care ar putea fi primit în linie de comandă)

import sys
import datetime as dt
from time import sleep


def get_seconds_from_now(timespec):
    #hour, minute = timespec.split(':')
    time = dt.time.strptime(timespec, '%H:%M')
    now = dt.datetime.now()

    then = now.replace(hour=time.hour, minute=time.minute, second=0)

    # if "then" is in the past,
    # then we need to look for tomorrow
    if then < now:
        then += dt.timedelta(days=1)

    diff = then - now

    return round(diff.total_seconds())


def countdown(seconds):
    l = len(str(seconds))
    while seconds:
        s = str(seconds).rjust(l, " ")
        print(f"waiting: {s}\r", end='')
        sleep(1)
        seconds -= 1

# întrebare:
# cum facem un hibrid library / executabil?

# răspuns:
# verificăm dacă suntem încărcați ca modul
# sau ca entry-point al aplicației

if __name__ == '__main__':
    # sunt aplicație
    # adică am fost rulat ca python filename.py
    #                    sau python -m filename
    try:
        timespec = sys.argv[1]
    except IndexError:
        # eroare de utilizare
        print("Usage: ceva cu bagă timestamp", file=sys.stderr)
        sys.exit(1)

    try:
        seconds = get_seconds_from_now(timespec)
    except ValueError:
        # altă eroare de utilizare
        print(f"Invalid timespec: '{timespec}'", file=sys.stderr)
        sys.exit(1)

    countdown(seconds)
    # maybe set an alarm, execute a payload etc...


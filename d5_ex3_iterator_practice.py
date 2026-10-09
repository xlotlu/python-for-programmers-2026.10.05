# Exercițiu
# dat fiind dataset-ul "data/temperatures.csv"
# ce conține (timestamp, value)
# cu timestamp garantate crescător,
#
# calculați mediile orare de temperaturi

import csv
from datetime import time

# modul clasic
from collections import defaultdict

def process_temps_classic(csvfile):
    temps = defaultdict(list)

    with open(csvfile) as f:
        reader = csv.reader(f)
        for tstamp, value in reader:
            value = float(value)
            tstamp = time.fromisoformat(tstamp)
            temps[tstamp.hour].append(value)

    return [
        (hour, sum(values) / len(values))
        for hour, values in
        temps.items()
    ]

from time import sleep


# vrem să avem acces frumos via atribute la fiecare
# record din csv

# nu facem așa, pentru că heavy-weight:
class TemperatureRecord:
    def __init__(self, tstamp, value):
        self.timestamp = tstamp
        self.value = value

# facem așa, much optimized:
from collections import namedtuple

# `namedtuple()` este un class factory:
TemperatureRecord = namedtuple('TemperatureRecord',
                               ['timestamp', 'value'])

# implementarea nouă de namedtuple,
# folosind syntaxa popularizată de pydantic
# (care, apropos, a fost implementată și ca dataclass)

from typing import NamedTuple

class TemperatureRecord(NamedTuple):
    timestamp: time
    value: float

def load_temps(csvfile):
    with open(csvfile) as f:
        for tstamp, value in csv.reader(f):
            value = float(value)
            tstamp = time.fromisoformat(tstamp)

            yield TemperatureRecord(tstamp, value)
            # simulăm un delay, cum ar fi la încarcare
            # de pe rețea / din amazon s3 / etc...
            sleep(.000001)


PRECISION_HOURLY = 0
PRECISION_MINUTES = 1

def process_temps(dataset, precision=PRECISION_MINUTES):
    total = 0
    count = 0

    _prev_ts = None
    for record in dataset:
        if precision == PRECISION_MINUTES:
            ts = record.timestamp.replace(second=0) # off, naming is hard.
        elif precision == PRECISION_HOURLY:
            ts = record.timestamp.replace(minute=0, second=0)

        # la fiecare schimbare de oră vrem să facem yield
        if _prev_ts is not None and ts != _prev_ts:
            yield TemperatureRecord(_prev_ts, total / count)

            total = 0
            count = 0

        total += record.value
        count += 1

        _prev_ts = ts

    yield TemperatureRecord(_prev_ts, total / count)


for elem in process_temps(
    load_temps("data/temperatures.csv"),
    PRECISION_HOURLY
):
    print(elem.timestamp, round(elem.value, 4))
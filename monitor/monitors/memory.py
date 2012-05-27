from monitor.functions import register
from monitor.helpers import read_file


def monitor_memory(record):
    "Monitors system memory"
    meminfo = read_file('/proc/meminfo')
    print meminfo
    for line in meminfo:
        tokenized_line = line.split()
        if len(tokenized_line) > 1:
            key, value = tokenized_line[:2]
            key = key.strip(':')
            record(key, value)

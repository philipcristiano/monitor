from monitor.functions import register
from monitor.monitors.base_monitor import BaseMonitor


def monitor_load(record):
    "Monitors system load"
    loadavg = open('/proc/loadavg').readall()
    load_values = loadavg.split()

    data = {
        '1_min': float(load_values[0]),
        '5_min': float(load_values[1]),
        '15_min': float(load_values[2]),
        'runnable_tasks': float(load_values[3].split('/')[0]),
        'total_tasks': float(load_values[3].split('/')[1]),
        'last_pid': float(load_values[4]),
    }

    for name, value in data.items():
        record(name, value)

register('load', monitor_load)

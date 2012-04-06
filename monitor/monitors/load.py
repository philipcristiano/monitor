from monitor.functions import register
from monitor.monitors.base_monitor import BaseMonitor


def monitor_load(record):
    "Monitors system load"
    loadavg = open('/proc/loadavg').readall()
    record('load {0}'.format(loadavg))


register('load', monitor_load)

import random

from monitor.functions import register

def monitor_random_data(record):
    "Records random information"
    record(random.random())

register('random_data', monitor_random_data)

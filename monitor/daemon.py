from multiprocessing import Process, Queue
import Queue
import time

import importlib

import monitor.functions
from monitor.runner import run_monitor
from monitor.publisher import start_publisher

config = {
    'monitors': ['random_data']
}

monitor_threads = {}

def load_monitors():
    "Load monitors from config"
    monitors = []
    for monitor_item in config['monitors']:
        monitor_name = 'monitor.monitors.{0}'.format(monitor_item)
        print monitor_name
        monitors.append(importlib.import_module(monitor_name))
    return monitors

def main():

    record_queue = Queue.Queue()
    publisher = start_publisher(record_queue)

    while True:
        load_monitors()
        for name, function in monitor.functions.monitors.items():
            old_thread = monitor_threads.get(name)
            if old_thread is None or not old_thread.is_alive():
                monitor_threads[name] = run_monitor(name, function, record_queue)
        time.sleep(1)

if __name__ == '__main__':
    main()

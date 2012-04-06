import threading
import time

from monitor.functions import record

def run_monitor(name, monitor_function):
    "Starts a monitor and returns a Thread"
    print 'starting', name
    thread = threading.Thread(
        target=_runner,
        name=name,
        args=[monitor_function, 5],
    )
    thread.daemon = True
    thread.start()
    return thread

def _runner(func, interval):
    while True:
        start = time.time()
        func(record)
        next_run = start + interval
        time.sleep(next_run - time.time())

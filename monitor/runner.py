import threading
import time

def run_monitor(name, monitor_function, queue):
    "Starts a monitor and returns a Thread"
    print 'starting', name
    thread = threading.Thread(
        target=_runner,
        name=name,
        args=[name, monitor_function, 5, queue],
    )
    thread.daemon = True
    thread.start()
    return thread

def _runner(name, func, interval, queue):
    def record(data):
        print name, data
        queue.put((name, data))

    while True:
        start = time.time()
        func(record)
        next_run = start + interval
        time.sleep(next_run - time.time())

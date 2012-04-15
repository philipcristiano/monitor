import socket
import threading

from monitor.connection import create_connection

def publish_target(queue):
    client = create_connection()
    hostname = socket.gethostname()


    while True:
        item = queue.get()
        routing_key = '{0}.{1}'.format(hostname, item[0])
        print 'publishing', item
        promise = client.basic_publish(
            exchange='monitor',
            routing_key=routing_key,
            body=str(item)
        )
        client.wait(promise)

def start_publisher(queue):
    thread = threading.Thread(
        target=publish_target,
        name='publisher',
        args=[queue],
    )
    thread.daemon = True
    thread.start()
    return thread


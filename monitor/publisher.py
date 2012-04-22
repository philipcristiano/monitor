import socket
import threading

from monitor.connection import create_zeromq_connection

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

def zeromq_publish_target(queue):
    print 'publisher starting'
    client = create_zeromq_connection()
    hostname = socket.gethostname()

    while True:
        item = queue.get()
        routing_key = '{0}.{1}'.format(hostname, item[0])
        to_send = [routing_key]
        to_send.extend(item)
        client.send_multipart(to_send)


def start_zeromq_publisher(queue):
    thread = threading.Thread(
        target=zeromq_publish_target,
        name='zeromq_publisher',
        args=[queue],
    )
    thread.daemon = True
    thread.start()
    return thread

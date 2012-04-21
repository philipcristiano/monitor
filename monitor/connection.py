import time

import zmq


def create_zeromq_connection():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind('tcp://*:5561')

    return publisher

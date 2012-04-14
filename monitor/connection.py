import puka

def create_connection():
    """Creates an AMQP connection"""
    client = puka.Client("amqp://33.33.33.10/")
    promise = client.connect()
    client.wait(promise)
    return client

import socket as python_socket
import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print "Reading metrics..."
socket.connect ("tcp://localhost:5561")

filter = sys.argv[1] if len(sys.argv) > 1 else python_socket.gethostname()
socket.setsockopt(zmq.SUBSCRIBE, filter)
print 'subscribed to', filter

while True:
    data = socket.recv_multipart()
    print data


monitors = {}

def record(data):
    print data

def register(name, function):
    monitors[name] = function



def read_file(filename):
    """Read the contents of :param:filename"""
    with open(filename, 'r') as f:
        return f.readall().split('\n')

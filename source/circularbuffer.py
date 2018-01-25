from hashtable  import HashTable


class CircularBuffer(object):
    #initialize a new circular buffer that can store at most max_size items
    def __init__(self, max_size):
        self.max = max_size
        self.data = []

    #property that tracks the number of items in the buffer
    def size(self):
        return self.size

    #check if the buffer is empty
    def is_empty(self):
        return self.head is None

    def is_full(self):
    #check if the buffer is full
    if self.data not is_empty():
        if len(self.data) == self.max:
        return ValueError('Buffer is full...')

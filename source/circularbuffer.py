from hashtable  import HashTable
from stack import ArrayStack


class CircularBuffer(object):
    #initialize a new circular buffer that can store at most max_size items
    def __init__(self, max_size=7):
        self.list = ArrayStack()
        self.max = max_size
        self.size = 0
        self.start = 3
        self.end = 0

    #check if the buffer is empty
    def is_empty(self):
        return self.start is None

    def length(self):
        return self.size

    def is_full(self):
    #check if the buffer is full

        if self.size == self.max:
            return ValueError('Buffer is full...')

    def enqueue(self, item):
        #insert item at the back of the buffer
        self.list.end.add(item)
        self.end += 1
        self.size += 1

    def front(self):
        #return the item at the front of the buffer
        if self.is_empty():
            return None
        return self.list[self.start]

    def dequeue(self):
        #remove and return the item at the front of the buffe
        if self.is_empty():
            raise ValueError

        new_start = self.list.remove(self.start)
        self.start += 1
        self.size -= 1

        if self.start == max_size:
            self.start = self.start - self.max


        return self.start


CircularBuffer = CircularBuffer

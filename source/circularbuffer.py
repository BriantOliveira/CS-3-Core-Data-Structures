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

    def enqueue(self, item):
        #insert item at the back of the buffer
        self.max.append(item)

    def front(self):
        #return the item at the front of the buffer
        if self.is_empty():
            return None
        return self.max.head.data

    def dequeue(self):
        #remove and return the item at the front of the buffe
        if self.is_empty():
            raise ValueError
        data = self.max.head.data

        if self.max.tail == self.max.head:
            self.max.head = None
            self.max.tail = None
        else:
            self.max.head = self.max.head.next
        return data

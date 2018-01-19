#!python

from doubly_linkedlist import Doubly_LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class Doubly_LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.head = None
        self.tail = None
        # self.size = 0
        self.list = Doubly_LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.head is None

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.length()
        print(self.length)


    def enqueue_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        #Append to the end of the list
        self.list.append(item)


    def enqueue_front(self, item):
        # TODO: Insert given item
        # Move the item to the start of the list
        self.list.prepend(item)



    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            #raise ValueError
            return None
        #return self.list.head.data
        self.list.pop(-1)

    def back(self):
        if self.is_empty():
            return None
        return self.list.tail.data

    def dequeue_front(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        #Check if head is empty
        if self.is_empty():
            raise ValueError

        #Set the data to the tail
        data = self.list.tail.data
        self.list.delete(self.list.tail.data)
        return data

    def dequeue_back(self):

        #Check if head is empty
        if self.is_empty():
            raise ValueError

        #Set the data to the head
        data = self.list.head.data
        self.list.delete(self.list.head.data)
        return data




# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
DoublyQueue = Doubly_LinkedQueue
# Queue = ArrayQueue

q = Doubly_LinkedQueue()
print(q.list)
q.enqueue_back('E')
print(q.enqueue_back('E'))
print(q.list)
print(q.enqueue_front('A'))
print(q.list)
print(q.enqueue_front('M'))
print(q.list)
print(q.enqueue_back('T'))
print(q.list)
print(q.front())
print(q.back())
print(q.list)
q.dequeue_back()
print(q.list)
q.dequeue_front()
print(q.list)
print(q.dequeue_front())
print(q.list)
q.dequeue_front()
print(q.list)
print(q.front())

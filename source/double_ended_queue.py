#!python

from doubly_linkedlist import Doubly_LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class Doubly_LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
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
    def push_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        #Append to the end of the list
        self.list.append(item)

    def push_front(self, item):
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
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        #Check if head is empty
        if self.is_empty():
            raise ValueError
        #Set the data to the head
        data = self.list.head.data

        #Check is the current node is the head and the tail
        if self.list.tail == self.list.head:
            self.list.head = None
            self.list.tail = None
        else:
            #If not move to the next node
            self.list.head = self.list.head.next
        return data



# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue

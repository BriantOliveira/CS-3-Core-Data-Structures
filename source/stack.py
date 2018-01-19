#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)


    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.head is None

    def size(self):
        return self.size

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items

        return self.list.length()


        # #Node count initialized to zero
        # node_count = 0
        # #Start at the head node
        # node = self.list.head
        # #Loop until the node is None, which is one node far past the tail
        # while node is not None:
        #     #Count one for this node
        #     node_count += 1
        #     #Skip to the next node
        #     node = node.next
        # #Now node count contain the amount of nodes
        # return node_count

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Push given item
        # new_node = self.list
        # #Give the data to the new node
        # new_node.data = data
        #
        # # if self.head:
        # self.head = new_node
        # self.head.next = next_node
        # self.size +=1

        #prepend to the head
        self.list.prepend(item)




    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any

        # Check if the head is empty

        # if  self.head:
        #     return self.head.data
        # else:
        #     return None

        if self.is_empty():
            return None

        return self.list.head.data


    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any

        #check if the node is is_empty
        if self.is_empty():
            #return None
            raise ValueError
        #remove and return object to the top
        # else:
        #     first_element = self.head
        #     self.head = first_element.next
        #     #Decrement the value of the size
        #     self.size -= 1
        #     #return data
        #     return first_element.data

        data = self.list.head.data

        if self.list.tail == self.list.head:
            self.list.head = None
            self.list.tail = None
        else:
            self.list.head = self.list.head.next
        return data

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack

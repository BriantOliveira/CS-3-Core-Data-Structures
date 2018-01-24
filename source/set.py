from hashtable import HashTable

class set(object):
    def __init__(self, elements=None):
        self.size = 0
        if elements is None:
            self.data = HashTable(4)
        else:
            self.data = HashTable(len(elements))

    def size(self):
        """Returns if its True, else is False"""
        return self.size

    def contains(self, element):
        """
        return a boolean indicating whether element is in this set
        """
        contain = self.data.contains(element)
        return contain
    def add(self, element):
        """ Add element to this set, if not present already """

        if element is not in self.data.keys():
             

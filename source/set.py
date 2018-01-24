from hashtable import HashTable

class Set(object):
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
             self.data.set(element, None)
             self.size += 1
        else:
            return ValueError("The element in set exit already")

    def remove(element):
        """Remove element from this set, if present, or else raise KeyError"""

        if element is in self.data.keys():
            self.data.delete(element)
            self.size -= 1
        else:
            return ValueError('The element does not exist in set')

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""

        new_set = Set(self.data.keys())

        for element in other_set.data.keys():
            if self.data.contains(element):
                continue

        else:
            new_set.data.append(element)

        return new_set

    def intersection(other_set):
        """
        return a new set that is the intersection of this set and other_set
        """
        if other_set.data and self.data is None:
            new_set = Set()

            for element in self.data.keys():
                if self.data.contains(element):
                    new_set.data.append(element)
                return new_set
            else:
                return ValueError("The set is empty...")

    def difference(other_set):
        """ return a new set that is the difference of this set and other_set """

        if other_set.data and self.data is None:
            new_set = Set()

            for element in self

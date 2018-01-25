from hashtable import HashTable

class Set(object):
    def __init__(self, elements=None):
        # property that tracks the number of elements in constant time
        self.size = 0
        # Initialize a new HashTable to store the set elements
        if elements is None:
            self.data = HashTable(4)
        else:
            self.data = HashTable(len(elements))

    def contains(self, element):
        """
        return a boolean indicating whether element is in this set
        """
        #Checking if the element is in the set
        return self.data.contains(element)

    def add(self, element):
        """ Add element to this set, if not present already """
        #Check if this element is in the set
        #if element not in self.data.keys():
        if not self.contains(element):
             self.data.set(element, None)
             # If the set is none add 1
             self.size += 1
             #print('HERE', element)
        else:
            return ValueError("Element {!r} already exists in set".format(element))

    def remove(element):
        """Remove element from this set, if present, or else raise KeyError"""

        #If the element is in the set
        if element in self.data.keys():
            # Delete the element
            self.data.delete(element)
            #Resize the set
            self.size -= 1
        else:
            return ValueError('The element does not exist in set')

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        #Create a new variable for the new set
        new_set = Set(self.data.keys())
        #Check is the other_set contain the element
        for element in other_set.data.keys():
            if self.data.contains(element):
                continue

            else:
                #Add the new element to the new_set
                new_set.add(element)

        return new_set

    def intersection(other_set):
        """
        return a new set that is the intersection of this set and other_set
        """
        #Check if the set is empty
        if other_set.data and self.data is None:
            new_set = Set()

            #Check if the set contain the element that we are looking for
            for element in self.data.keys():
                if self.data.contains(element):
                    #Add the element to the new set
                    new_set.add(element)
                return new_set
            else:
                return ValueError("The set is empty...")

    def difference(other_set):
        """ return a new set that is the difference of this set and other_set """
        #Check if the set is empty
        if other_set.data and self.data is None:
            new_set = Set()
            #Check if the set contains the element, if so remove
            for element in self.data.keys():
                if self.data.contains(element):
                    new_set.data.remove(element)

            new_set = self.data.keys()
            return new_set

    def is_subset(other_set):
        """return a boolean indicating whether other_set is a subset of this set"""

        if other_set and self.data is not None:
            for element in self.data.keys():
                if self.data.contains(element):
                    continue
                else:
                    return False
            return True

def test_set():
    new_set = Set()
    new_set.add("Hello")
    new_set.add("v")
    new_set.contains("world")
    new_set.add("k")
    other_set = Set()
    other_set.add('why')
    other_set.add("l")
    set_test = new_set.union(other_set)
    #inter_set = new_set.intersection(other_set)
    print(new_set.data)
    print(other_set.data)
    print(set_test.data)

if __name__ == '__main__':
    test_set()

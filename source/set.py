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
        #Return the size of the set
        return self.size

    def contains(self, element):
        """
        return a boolean indicating whether element is in this set
        """
        #Checking if the element is in the set
        contain = self.data.contains(element)
        return contain

    def add(self, element):
        """ Add element to this set, if not present already """
        #Check is there is a element in the set
        if element is not in self.data.keys():
             self.data.set(element, None)
             # If the set is none add 1
             self.size += 1
        else:
            return ValueError("The element in set exit already")

    def remove(element):
        """Remove element from this set, if present, or else raise KeyError"""

        #If the element is in the set
        if element is in self.data.keys():
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
            new_set.data.append(element)

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
                    new_set.data.append(element)
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

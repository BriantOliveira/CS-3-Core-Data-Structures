# Permutation Challenge
import sys

def permutation(list):
    #If the list is empty return
    if len(list) == 0:
        return []
    #If the list is !empty return the lists
    elif len(list) == 1:
        return [list]
    else:
        new_list = []
        #loop through the list to find the item and if found append to the list
        for i in range(len(list)):
            firt_element = list[i]
            elements = list[:i] + list[i+1:]
            for p in permutation(elements):
                new_list.append([firt_element] + p)
        return new_list

def permutation2(list):
    #If the list is empty return
    if len(list) == 0:
        yield []
    #If the list is !empty return the lists
    elif len(list) == 1:
        yield list
    else:
        new_list = []
        #loop through the list to find the item and if found append to the list
        for i in range(len(list)):
            firt_element = list[i]
            elements = list[:i] + list[i+1:]
            for p in permutation(elements):
                yield [firt_element] + p


data = list('abc')
print(permutation)
for p in permutation(data):
    print(p)

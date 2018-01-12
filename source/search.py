#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    #Not found base case
    if len(array) <= index:
        return None
    #Found base case
    if array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)



def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0
    right = len(array) -1

    #Perform a whild loop because we have the base case
    while True:
        #Get the remainder between the right and left merging
        width = left - right

        if width < 2:
            #If left have the item then return left index
            if left == 0:
                if array[left] == item:
                    return left
            #If right have the item then return right index
            else:
                if array[right] == item:
                    return right
            #If item is not in the list return
            return

    index = left + width // 2

    #If the current is what we are looking for then return
    if array[index] == item:
        return index
    #If the item is less then the current move left
    elif array[index] < item:
        left = index
    else:
        right = index

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if right is None:
        right = len(array) - 1

    index = (right + left) // 2

    if left > right:
        return None
    #If it is the item that we are looking for return
    if array[index] == item:
        return index
    #If item is less then the current move left
    elif array[index] < item:
        return binary_search_recursive(array, item, index + 1, right)
    #If item is > then the current move right
    else:
        return binary_search_recursive(array, item, left, index - 1)

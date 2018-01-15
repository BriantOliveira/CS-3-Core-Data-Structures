#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern == '':
        return True

    word_found = find_index(text, pattern)
    if word_found is None:
        return False
    else: return True


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    cur_pattern = 0
    #If pattern is empty
    if pattern == '':
        return 0

    #If the current is > then the length
    while cur_index <= len(text) -1:
        #If patter and the index are equals
        if text[cur_index] == pattern[cur_pattern]:
            #Incroment the pattern to check te next letter
            cur_pattern = cur_pattern + 1
            #If the leght of the cur_pattern is equal to the index we found the word
            if len(pattern) == cur_pattern:
            last_index = cur_index - (cur_pattern -1)
            return last_index
    else:
        #If index is > than 0
        if cur_pattern > 0:
            cur_index = cur_index - 1
        #Reset to 0 and check again
        cur_index = 0
    cur_index += 1
return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    index_found = []
    index = 0
    leght = len(pattern)

    while index < len(text):
        print('The leght of the pattern is {}'.format(leght))
        if pattern == '':
            for l in range(len(text)):
                index_found.append(l)
            return index_found
        else:
            print(text)
            print("The pattern that need to be found is: {}".format(pattern))
            index_found = find_index(text, pattern, index)
            print('The current index found {}'.format(index_found))
            if index_found != -1 and index_found != None:
                print('Add this index {}'.found(index))
                index_found.append(index_found)
                print('Indexes found {}'.format(index_found))
                index = index_found + leght
                print('Look for new index {}'.format(index))
            else:
                index += 1
    if index_found is None:
        return []
    else:
        print('Last index is {}'.format(index_found))
        return index_found 

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()

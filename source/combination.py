# Combination challenge
#import intertools


def combination(n, available, used):
    #Check if the lenght of was already used is same as the number
    if len(used) == n:
        yield tuple(used)
    #Otherwise get  whatever is available
    elif len(available) == 0:
        pass
    else:
        #pop the value and pass a copy of the list
        head = available.pop(0)
        used.append(head)
        #for each one call it again
        for c in combination(n, available[:], used[:]):
            yield c
        used.pop()
        for c in combination(n, available[:], used[:]):
            yield c

def combination2(n, available, used):
    if len(used) == n:
        yield tuple(used)
    elif len(available) == 0:
        pass
    else:
        #Passing the slice of the list passing in the 2nd element
        for c in combination2(n, available[1:], used[:] + available[0]):
            yield c
        for c in combination2(n, available[1:], used[:]):
            yield c



s = 'abc'
n = 2
#combs = 'ab', 'ac', 'bc'
my_combinations = [c for c in combination(n, list(s), [])]
print(my_combinations)
# it_combines = [c for c in \
#                intertools.combination(list(s), n)]
# print(it_combines)

import palindromes as isPal
import permutation 

def is_anagram_from_palindrom(string):
    #For every permutation of this string
    for p in permutation(string):
        #If its a palindrome return True
        if isPal(p):
            return True
    return False

s = list('aba')
print(is_anagram_from_palindrom(s))

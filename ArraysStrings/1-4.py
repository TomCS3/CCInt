"""
Pallidrome Permutation: Given a string, write a function to check if it is a permutation of a palin- drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""

def permutation_palidrome(str1):
    """
    Time complexity O(n) where n is the length of the string
    space complexity O(n) 
    """
    dict1 = {}
    odd_count=0
    for char in str1:
        if char in dict1:
            dict1[char] +=1
        else:
            dict1[char] = 1
    for elem in dict1:
        if odd_count > 1:
            return False
        if dict1[elem] % 2 != 0:
            odd_count +=1
    return True

def permutation_palidrome_bit(s):
    """
    Time complexity O(n) where n is the length of the string
    space complexity O(1) as bit vector is 128 elements in length regardless
    """
    if s is None:
        return True
    bit_vector = 128*[False]
    for char in s:
        if 0 <= ord(char) <= 127 and char != ' ':
            bit_vector[ord(char)] = not bit_vector[ord(char)] # flips the bit
    if sum(bit_vector) == 0 or sum(bit_vector) == 1:
        return True
    else:
        return False



print(permutation_palidrome('assddffaa'))
print(permutation_palidrome_bit('asssddffaa'))
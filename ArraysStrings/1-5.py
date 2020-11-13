"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, pIe -> true
 pales. pale -> true
pale. bale -> true 
pale. bake -> false
"""

def insert_or_replace(s1, s2):
    if len(s1) == len(s2):
        return replace(s1,s2)
    elif len(s1) + 1 == len(s2):
        return insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return insert(s2, s1)
    else:
        return False

def replace(s1, s2):
    i, j = 0, 0
    difference = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if difference:
                return False
            difference = True
        i += 1
        j += 1
    return True

def insert(s1, s2):
    i, j = 0, 0
    difference = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if difference:
                return False
            difference = True
            i += 1
        else:
            i += 1
            j += 1
    return True

print(insert_or_replace('acde', 'acdb')) # True
print(insert_or_replace('acde', 'ace')) # True
print(insert_or_replace('acde', 'accc')) # false
print(insert_or_replace('ac', 'acdb')) # false 
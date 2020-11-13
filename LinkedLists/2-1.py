"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
"""


def delete_duplicate(lst: list) -> list:
    """ 
    Creates a dictionary from the list and returns a list of the keys.
    As a dictionary cannot have duplciate keys it the return list has no duplicates
    """
    return list(dict.fromkeys(lst))

print(delete_duplicate([1,2,2,3,3,4,5,6,6,6])) 
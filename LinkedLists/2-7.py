"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based on reference,
not value. That is, if the kth node of the first linked list is the exact 
same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""

def Intersection(l1, l2):
    if l1 == None or l2 == None:
        return False
    
    # Return the tail and the length of the two lists
    p1, p2 = l1, l2
    length1, length2 = 0, 0
    while p1 != None:
        length1 += 1
        p1 = p1.next
    while p2 != None:
        length2 += 1
        p2 = p2.next
    
    if p1 != p2:
        return False


    p1, p2 = l1, l2
    length_diff = length1 - length2
    if length_diff > 0:
        for i in range(length_diff):
            p1 = p1.next
    elif length_diff < 0:
        for i in range(abs(length_diff)):
            p2 = p2.next
    
    while p1 != None:
        if p1 == p2 and p1.next = p2.next:
            return True
        p1 = p1.next
        p2 = p2.next 
    
    return False


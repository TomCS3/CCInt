"""
2.2 Return Kth to Last: Implement an algorithm to find the kth 
to last element of a singly linked list.
"""
# This algorithm takes O( n) time and O( 1) space.
def return_kth_to_last(head, k):
    if k<=:
        return None

    p1 = head
    p2 = head

    for i in range(k):
        if p1 == None:
            return None
        p1 = p1.next
    
    while p1 != none:
        p1 = p1.next
        p2 = p2.next
    
    return p2
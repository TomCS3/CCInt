"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINI TION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
SOLUTION
EXAMPLE
Input: A -> B -> C -> D -> E -> C[thesameCasearlier) Output: C
"""

def FindStart(head):
    slow = head
    fast = head

    # advance the fast pointer at twice the rate of the slow until they collide
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        
    # Check for error, i.e not a loop
    if fast == None or fast.next == None:
        return False
    
    # By moving the slow pointer to the head, both pointers are k steps away
    # from the start of the loop
    slow = head
    while slow !=fast:
        slow = slow.next
        fast.next

    # Both Pointers are at the start of the loop
    return fast
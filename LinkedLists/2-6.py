"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

def palidrome(head):
    if not head:
        return False

    if head.next == None:
        return True

    # Find the length of the LL
    p1 = head
    length = 0
    while p1.next != None:
        length += 1
        p1 = p1.next

    # Determine the start point of the reversed List
    half_length = length // 2
    if length % 2 == 0:
        start = half_length
    else:
        start = half_length + 1

    # Advances the counter to the middle.
    p1 = head
    for i in range (half_length - 1):
        p1 = p1.next
    
    # Creates a reverse of the second half of the Linked list 
    revList = SLinkedList()
    while p1 != None:
        revList.add(p1.data)

    # Compare the lists
    p1 = head
    p2 = revList.head
    while p2 != None:
        if p1 != p2:
            return False
        p1 = p1.next
        p2 = p2.next
    
    return True

# Create Test Linked List
testList = SLinkedList()
testList.add(1)
testList.add(2)
testList.add(3)
testList.add(3)
testList.add(2)
testList.add(1)

print (palidrome(testList.head))

# TBC
 


    

      

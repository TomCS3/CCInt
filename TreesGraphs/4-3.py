"""
List of Depths: Given a binary tree, design an algorithm which creates a 
linked list of all the nodes at each depth (e.g., if you have a tree with 
depth 0, you'll have 0 linked lists).
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        

def createLL(root, lists, level):
    if root == None:
        return
    
    list = None

    if (len(lists) == level): # level not contained in list
        list = LinkedList()
        lists.insert(list)
    else:
        list = lists.find


"""To be finished"""

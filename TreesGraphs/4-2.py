"""
4.2 Minimal Tree: Given a sorted (increasing order) array
 with unique integer elements, write an algorithm to create
 a binary search tree with minimal height.
"""
class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
def buildBST(arr):
    if not arr:
        return None

    # Find Middle
    mid = (len(arr)) //  2

    # Make middle element root
    root = Node(arr[mid])

    root.left = buildBST(arr[:mid])

    root.right = buildBST(arr[mid+1:])

    return root


# A utility function to print the preorder  
# traversal of the BST 
def preOrder(node): 
    if not node: 
        return
      
    print(node.data) 
    preOrder(node.left) 
    preOrder(node.right)  
  
# driver program to test above function 
""" 
Constructed balanced BST is  
    4 
/ \ 
2 6 
/ \ / \ 
1 3 5 7 
"""
  
arr = [1, 2, 3, 4, 5, 6, 7] 
root = buildBST(arr) 
print("PreOrder Traversal of constructed BST ") 
preOrder(root) 
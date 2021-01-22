"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements into any other
data structure (such as an array). The stack supports the following operations: push, pop, 
peek, and isEmpty.
"""

class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.isEmpty:
            return None
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.isEmpty:
            return None
        else:
            return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

def SortStack(uStack):

    tStack = Stack()

    while not uStack.isEmpty():
        tmp = uStack.pop()
        while not tStack.isEmpty and tStack.peek() > tmp:
            uStack.push(tStack.pop())
        tStack.push(tmp)
    
    while not tStack.isEmpty():
        uStack.push(t.pop())




    # sortedStack = Stack()
    # tempStack = Stack()
    # sortedStack.push(unsortedStack.pop())
    # while not unsortedStack.isEmpty():
    #     if unsortedStack.peek() >= sortedStack.peek():
    #         sortedStack.push(unsortedStack.pop())
    #     else:
    #         while unsortedStack.peek() < sortedStack.peek():
    #             tempStack.push(sortedStack.pop())
    #         sortedStack.push(unsortedStack.pop())
    #         while not tempStack.isEmpty:
    #             sortedStack.push(tempStack.pop())
    # return sortedStack



        
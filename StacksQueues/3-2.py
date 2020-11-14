"""
Stack Min: How would you design a stack which, in addition to push and pop,
 has a function min which returns the minimum element? Push, pop and min 
 should all operate in 0(1) time.
"""
class MinStack:

    def __init__(self):
        self.elemStack = []
        self.minStack = []

    def size(self):
        return len(self.elemStack)

    def isEmpty(self):
        return len(self.elemStack) == 0
    
    def push(self, item):
        if self.size() == 0:
            self.minStack.append(item)
        elif item < self.minStack[-1]:
            self.minStack.append(item)
        self.elemStack.append(item)

    def pop(self):
        if isEmpty:
            raise ValueError("Stack Empty")
        item = self.elemStack.pop()
        if item == self.minStack[-1]:
            self.minStack.pop()
        return item
  
    def min(self):
        return self.minStack[-1]





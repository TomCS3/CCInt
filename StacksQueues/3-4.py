"""
3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""

class MyQueue:

    def __init__(self):
        self.stackNewest = stack()
        self.stackOldest = stack()

        def size(self):
            return len(self.stackNewest) + len(self.stackOldest)
        
        def add(self, item):
            self.stackNewest.append(item)
        
        def shiftStacks(self):
            if stackOldests.isEmpty():
                while not stackNewest.isEmpty():
                    stackOldest.push(stackNewest.pop())

        def peek(self):
            shiftStacks()
            return stackOldest.peek()
        
        def remove(self):
            shiftStacks()
            return stackOldest.pop()
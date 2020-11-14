"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, 
it might topple. Therefore, in real life, we would likely start a new stack when
the previous stack exceeds some threshold. Implement a data structure SetOfStacks 
that mimics this. SetOfStacks should be composed of several stacks and should 
create a new stack once the previous one exceeds capacity. SetOfStacks. push () 
and SetOfStacks. pop() should behave identically to a single stack (that is, pop ( )
should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub- stack.
"""

class stack:

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def isFull(self):
        return self.stack.size() == capacity
    
    def isEmpty(self):
        return self.stack.size() == 0
    
    def size(self):
        return len(self.stack)
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
class setofstacks:

    def __init__(self, stackCapacity):
        self.stacks =[stack(stackCapacity)]
        self.currentStack = 0
        self.stackCapacity = stackCapacity
    
    def push(self, item);
        if self.stacks[self.currentStack].isFull():
            self.stacks.append[stack(stackCapacity)]
            self.currentStack += 1
        self.stacks[self.currentStack].push(item)

    def pop(self):
        if self.stacks[self.currentStack).isEmpty()]:
            if self.currentStack == 0:
                return ValueError("Stacks are empty")
            self.currentStack -= 1
        self.stacks[self.currentStack].pop(item)


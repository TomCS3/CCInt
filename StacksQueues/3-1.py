"""
How to use a single array to implement three stacks
"""

class FixedMultiStack:
    """
    fixed size array
    """
    def __init__(self, numberOfStacks, stackSize):
        self.numberOfStacks = numberOfStacks
        self.stackCapacity = stackSize
        self.values = [0] * (stackSize * k)
        self.sizes = [0] * stackNum
    
    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity
    
    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    def push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception("Stack is Full")
        self.sizes[stackNum] += 1 # increases pointer
        self.values[indexTop(stackNum)] = item

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception("Stack is Empty")
        self.sizes[stackNum] -= 1
        # Clears but not necessary pointer to top of stack is what matters
        self.values[indexTop(stackNum)] = 0 
    
    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception("Stack is Empty")
        return self.values[indexTop(StackNum)]

    def indexTop(self, stackNum):
        offset = stackNum * stackCapacity
        size = self.sizes[stackNum]
        return offset + size - 1

class MultiStack:
    """
    For dynamically sized stacks in a fixed array
    NOTE: next array determines either the previous element in the stack if popping
          or the next free space after free has been used if pushing.
    """

    def __init__(self, numberOfStacks, arraySize)
        self.numberOfStacks = numberOfStacks
        self.arraySize = arraySize
        self.values = [0] * self.arraySize
        self.top = [-1] * self.numberOfStacks
        self.free = 0

        # Initialises the next / previous array
        self.next = [i + 1 for i in range(arraySize)]
        self.next[self.arraySize - 1] = -1

    def IsEmpty(self, stackNum):
        return self.top[stackNum] == -1

    def IsFull(self):
        return self.free == -1

    def push(self, stackNum, item):
        if self.IsFull(stackNum):
            print("Stack Overflow")

        # Current free index in the array for the item to be inserted
        insert_at = self.free

        # Updates the free index to the next 
        # available free index as per next array 
        self.free = self.next[self.free]

        # Updates the array to contain the item
        self.values[insert_at] = item

        # Adjusts the next pointer at that index to 
        # point to the old top of the stack
        self.next[insert_at] = self.top[stackNum]

        # Sets the pointer to the new top of the stack
        self.top[stackNum] = insert_at


    def pop(self, stackNum)
        if self.IsEmpty(stackNum):
            print("Stack is empty")

        # Current stack top    
        stack_top = self.top[stackNum]

        # Updates to new top of the stack
        self.top[stackNum] = self.next[self.top[stackNum]]

        # Updates the next free element to the 
        # current free element for a later submission
        self.next[stack_top] = self.free

        # Sets the free element to the element space which has been popped
        self.free = elem_pop

        return self.value[stack_top]
class MinStack:
    def __init__(self):
        self.stack = []      # Regular stack
        self.minStack = []   # Stack of minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Push the current minimum
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()  # Pop from both!

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]  # Top of minStack is always the min
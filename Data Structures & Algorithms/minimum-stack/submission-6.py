class MinStack:

    def __init__(self):
        # Create two stacks assocaited with the object.
        self.stack = [] # Acts as a regular stack.
        self.min_stack = [] # Holds the current minimum at any given time.

    def push(self, val: int) -> None:
        # Always append values to the regular stack.
        self.stack.append(val)
        
        # Append the current min to the top of the stack, whether its a previous min,
        # or if the new element is a new minimum.
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        # Pop the top element from the top of both stacks.
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]        

class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        
        # Case A: There's nothing in the stack 
            # Insert the value and set default
        # Case B: The value inserted in the stack is greater than the min [value, currentMin]
            # Insert [value, currentMin]
        # Case C: The  value inserted is less than the current min
            # Replace the current min and insert item [value, value]
        if (self.size == 0):
            self.stack.insert(0, [val, val])
        else:
            curMin = self.stack[0][1]
            if (val > curMin):
                self.stack.insert(0, [val, curMin])        
            else: # (val < curMIn):
                self.stack.insert(0, [val, val])
        self.size += 1
        
    def pop(self) -> None:
        if (self.size != 0):
            self.stack.pop(0)
            self.size -= 1
        return None
        
    def top(self) -> int:
        if (self.size != 0):
            return self.stack[0][0]
        return None
        
    def getMin(self) -> int:
        if (self.size != 0):
            return self.stack[0][1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
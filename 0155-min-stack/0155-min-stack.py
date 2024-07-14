class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
        

    def pop(self) -> None:
        v = self.stack.pop()
        if self.min == v:
            self.min = 2**31
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        for i in self.stack:
            if i < self.min:
                self.min = i
        return self.min
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
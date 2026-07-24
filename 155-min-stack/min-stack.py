class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_x=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        current=value if not self.min_x else min(self.min_x[-1],value)
        self.min_x.append(current)
    def pop(self) -> None:
        self.stack.pop()
        self.min_x.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_x[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
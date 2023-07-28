class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val):
        self.stack.append(val)
        if self.minVal:
            if val <= self.minVal[len(self.minVal) - 1]:
                self.minVal.append(val)
            else:
                self.minVal.append(self.minVal[len(self.minVal) - 1])
        else:
            self.minVal.append(val)
        

    def pop(self):
        self.stack.pop()
        self.minVal.pop()
        

    def top(self):
        return self.stack[len(self.stack) - 1]
        

    def getMin(self):
        return self.minVal[len(self.minVal) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
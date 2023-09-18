class MinStack:
    

    def __init__(self):
      self.stack = []
      
    def push(self, val: int) -> None:
      self.stack.append(val)
        

    def pop(self) -> None:
      self.stack.pop(self.stack[-1])
        
    def top(self) -> int:
      return self.stack[-1] 

    def getMin(self) -> int:
      return min(self.stack)


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin()
obj.pop()
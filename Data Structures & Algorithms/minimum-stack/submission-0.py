class MinStack:

    def __init__(self):
        self.stack = []
        self.min = int
    def push(self, val: int) -> None:
        self.stack.append(val)


    def pop(self) -> None:
        
        self.stack.pop()
    def top(self) -> int:
        
        return self.stack[-1]
    def getMin(self) -> int:
        miin = float('inf')
        for i in range(len(self.stack)):
            miin = min(miin, self.stack[i])
        return int(miin)

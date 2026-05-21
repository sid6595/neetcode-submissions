

class MinStack:

    def __init__(self):
        self.minimap = {}
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1
        if self.length == 1:
            self.minimap[self.length] = val
        else:
            self.minimap[self.length] = min(self.minimap[self.length-1], val)

    def pop(self) -> None:
        self.stack.pop()
        self.length -= 1

    def top(self) -> int:
        return self.stack[self.length-1]

    def getMin(self) -> int:
        if self.length != 0:
            return self.minimap[self.length]
        else:
            print("empty array")
            return self.mini

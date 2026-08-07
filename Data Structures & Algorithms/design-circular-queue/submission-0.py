class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.elements = []
        

    def enQueue(self, value: int) -> bool:
        if len(self.elements) == self.size:
            return False
        queue = deque(self.elements)
        queue.append(value)
        self.elements = list(queue)
        return True

    def deQueue(self) -> bool:
        if len(self.elements) == 0:
            return False
        queue = deque(self.elements)
        queue.popleft()
        self.elements = list(queue)
        return True

    def Front(self) -> int:
        if len(self.elements) == 0:
            return -1
        
        return self.elements[0]
        

    def Rear(self) -> int:
        if len(self.elements) == 0:
            return -1
        
        return self.elements[-1]        

    def isEmpty(self) -> bool:
        if len(self.elements) == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if len(self.elements) == self.size:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
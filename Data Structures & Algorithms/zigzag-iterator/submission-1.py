class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.ind1 = 0
        self.len1 = len(v1)
        self.v2 = v2
        self.ind2 = 0
        self.len2 = len(v2)
        self.alternate = True if self.ind1 < self.len1 else False
        self.progress = []

    def next(self) -> int:
        if self.alternate:
            cur = self.v1[self.ind1]
            self.ind1 += 1
            if self.ind2 != len(self.v2):
                self.alternate = not self.alternate
        else:
            cur = self.v2[self.ind2]
            self.ind2 += 1
            if self.ind1 != len(self.v1):
                self.alternate = not self.alternate
        
        self.progress.append(cur)
        return cur
        

        
    def hasNext(self) -> bool:
        if self.ind1 < self.len1 or self.ind2 < self.len2:
            return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

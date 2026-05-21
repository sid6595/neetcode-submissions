class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        resSet = []
        self.helper(1, [], resSet, n, k)
        return resSet
    
    def helper(self, i, curSet, resSet, n, k):
        if len(curSet) == k:
            resSet.append(curSet.copy())
            return
        if i > n:
            return
        
        curSet.append(i)
        self.helper(i+1, curSet, resSet, n, k)
        curSet.pop()

        self.helper(i+1, curSet, resSet, n, k)
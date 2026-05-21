class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)
    
    def helper(self, i, nums):
        if i >= len(nums):
            return [[]]
        
        resSet = []
        perms = self.helper(i+1, nums)
        for p in perms:
            for item in range(len(p)+1):
                pcopy = p.copy()
                pcopy.insert(item, nums[i])
                resSet.append(pcopy)
        return resSet

        
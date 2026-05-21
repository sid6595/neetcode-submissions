class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # O(n log n), doesn't matter since this is 2^n anyway
        new = nums.sort()
        resSet, curSet = [], []
        self.helper(0, nums, curSet, resSet)
        return resSet
    
    def helper(self, i, nums, curSet, resSet):
        if i >= len(nums):
            resSet.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i+1, nums, curSet, resSet)
        curSet.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        
        self.helper(i+1, nums, curSet, resSet)
        


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resSet, curSet = [], []
        self.helper(0, nums, curSet, resSet)
        return resSet

    def helper(self, i, nums, curSet, resSet):
        if i >= len(nums):
            resSet.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, resSet)
        curSet.pop()

        self.helper(i + 1, nums, curSet, resSet)
        
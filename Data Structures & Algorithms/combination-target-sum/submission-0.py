class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resSet = []
        self.helper(0, nums, resSet, [], target)
        return resSet
    
    def helper(self, i, nums, resSet, currentSet, target):
        if sum(currentSet) == target:
            resSet.append(currentSet.copy())
            return
        if i >= len(nums) or sum(currentSet) > target:
            return
        
        currentSet.append(nums[i])
        self.helper(i, nums, resSet, currentSet, target)
        currentSet.pop()
        self.helper(i+1, nums, resSet, currentSet, target)
        


        
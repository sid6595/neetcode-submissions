class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        memo = {}

        def dfs(i, target_sum):
            if target_sum == 0:
                return True 

            if i == len(nums):
                return False
            
            if (i, target_sum) in memo:
                return memo[i, target_sum]
            
            memo[i, target_sum] = dfs(i+1, target_sum) or dfs(i+1, target_sum - nums[i])

            return memo[i, target_sum]

        return dfs(0, target)


        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        current_sum = 0
        res = len(nums) + 1

        for r in range(0, len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                res = min(res, r - l + 1)
                current_sum -= nums[l]
                l += 1
        
        return res if res != len(nums) + 1 else 0

        
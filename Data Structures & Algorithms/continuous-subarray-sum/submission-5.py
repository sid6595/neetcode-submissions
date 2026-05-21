class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curSum = 0
        seen = {0:-1}

        for index, num in enumerate(nums):
            curSum += num
            remainder = curSum % k
            if remainder in seen and index - seen[remainder] > 1:
                return True
            seen[remainder] = seen.get(remainder, index)
        
        return False

        
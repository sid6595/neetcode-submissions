import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            searching_for = target - nums[i]
            if searching_for in seen:
                return [seen[searching_for], i]
            seen[nums[i]] = i
        print(seen)
        return []
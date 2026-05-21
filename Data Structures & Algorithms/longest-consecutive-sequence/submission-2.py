class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of = set(nums)

        curmax = 0

        for num in nums:
            if num - 1 not in nums:
                i = 0
                while num + i in nums:
                    i += 1
                    curmax = max(curmax, i)
                    
        return curmax


        
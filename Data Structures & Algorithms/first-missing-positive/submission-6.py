# given: unsorted integer array
# output: smallest POSITIVE integer NOT PRESENT in nums

# example
# [-2, -1, 0] -> 1
# [1, 2, 4] -> 3

# key info
# TC: O(n), SC: O(1)
# can't store any array/dict of what we've seen
# can only look at each element once

# [1,2,4,3] 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        
        """
        -1,2,4,5,6,3,1

        

        """

        for i in range(len(nums)):
            real = abs(nums[i])
            if real > 0 and real <= len(nums):  
                if nums[real-1] == 0:
                    nums[real-1] = -1 * real             
                else:
                    nums[real-1] = abs(nums[real-1]) * -1
        
     
        
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i

        return len(nums) + 1
        

        
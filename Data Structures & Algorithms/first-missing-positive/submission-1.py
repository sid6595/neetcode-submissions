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
        seen = defaultdict(int)

        for num in nums:
            seen[num] = 1
        
        i = 1
        while True:
            if i in seen:
                i += 1
            else:
                return i
        
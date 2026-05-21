# input
# array w/ length 'n' rotated between 1 and n times

# output
# return minimum element

# info
# all nums are unique
# will there always be a solution? -> nums = []

# O(log n)
# binary search, sorted
# find the pivot point
# this is going to be the minimum

# 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # l < r instead of l <= r
        # we want to find the pivot point
        # once l = r that's our solution
        while l < r:
            m = (l + r) // 2
            # we are in the right sorted portion
            if nums[m] > nums[r]:
                l = m + 1
            # left sorted portion
            else:
                r = m
        
        return nums[l]


        
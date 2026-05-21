# 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            # m < r 
            # case 1 -> midpoint is in the right sorted portion
            # pivot is in the left side (including midpoint)
            if nums[mid] < nums[r]:
                r = mid
            # m >= r
            # case 2 -> midpoint is in the left sorted portion
            # pivot is in the right side (not including midpoint)
            else:
                l = mid + 1
        
        return nums[l]
        
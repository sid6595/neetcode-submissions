class Solution:
    # binary search
    # find the pivot point using binary search
    # take the element to the right of the pivot or the beginning
    # minimum is the pivot point
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2
            if nums[mid] >= nums[l]: # pivot is to the right
                l = mid + 1
            else: # pivot is to the right or here
                r = mid
        
        return nums[l]
            
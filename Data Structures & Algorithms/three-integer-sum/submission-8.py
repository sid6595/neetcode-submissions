class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create dictionary of all possible 2 sum combos
        # look for complement of all these

        nums = sorted(nums) # O (n log n)
        output = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == -num:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > -num:
                    r -= 1
                else:
                    l += 1
            
        return output
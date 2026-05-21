# [1, 3, 4]
# [12, 4, 3]

# cases
# [0, 3, 4, 5] -> [60, 0, 0, 0]
# [0, 3, 4, 0] -> [0, 0, 0, 0]

# calculate product of all numbers before and after
# create those arrays
# loop again and multiply those values


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # [1, 2, 3]

        # [1, 1, 2]
        # [6, 3, 1]

        prefix[0] = 1
        suffix[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            """
            [1, 1, 1]
            [1, 1, 2]
            """
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            """
            3 - 2 = 1
            [1, 1, 1] 
            [1, 3, 1]
            [6, 3, 1]
            """
            suffix[j]= nums[j+1] * suffix[j+1]
        
        print(prefix)
        print(suffix)
        
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        
        return result

        


        
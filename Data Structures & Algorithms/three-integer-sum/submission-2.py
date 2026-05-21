# array nums, unsorted
# goal: all triplets where the sum == 0
# must be distinct

# cases 
# [-1, -1, 0, 1] -> 2

# nums[i] + nums[j] = -nums[k]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums) # O(n log n)
        result = []

        for index, num in enumerate(sorted_array):
            L, R = index + 1, len(sorted_array) - 1
            # [a, L, x, x, R]
            # [x, a, L, x, R]

            """
            0, -1

            1 -> -1, 3 -> 1, sum: 0, target: 1
            2, 3, 0
            """
            if index > 0 and num == sorted_array[index - 1]:
                continue
            while L < R:
                sum_val = sorted_array[L] + sorted_array[R]
                if sum_val > -num:
                    R -= 1
                elif sum_val < -num:
                    L += 1
                else:
                    result.append([num, sorted_array[L], sorted_array[R]])
                    L += 1
                    R -= 1
                    while sorted_array[L] == sorted_array[L-1] and L < R:
                        L += 1
        
        return result
                


# array of ints : increasing or equal order
# index 1 and 2 cannot be equal
# one valid solution
# O(1) space

# cases
# [1,1,3,4] , 7

# 2 pointers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        """
        0, 3, 5
        1, 3, 5
        2, 3, 7
        """
        while L < R:
            total = numbers[L] + numbers[R]
            if total == target:
                return [L+1, R+1]
            if total > target:
                R -= 1
            if total < target:
                L += 1
        
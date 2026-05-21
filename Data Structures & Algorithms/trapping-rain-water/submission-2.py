# input: array of non-negative ints -> heights
# output: int -> maximum area of water thats trapped

# examples
# [2,0,3] -> 2
# [] -> Constraint
# [5] -> 0
# [4,3] -> 0

# observations
# impossible to hold water in the first or last element
# need a left and right wall to bound our water at each position
# if left or right wall < height[i], no water -> set new wall height

# 2 pointer
# start a pointer on each end
# store maxLeft and maxRight
# compare these at each iteration
# if maxLeft > maxRight -> move right pointer
# else move left pointer
# do water calculation -> minWallheight - height[i]

# TC: O(n)
# SC: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        result = 0

        """
        [0,2,0,3]
        left, maxLeft, right, maxRight
        0, 0, 3, 3 -> 0
        1, 2, 3, 3 -> 0
        2, 2, 3, 3 -> 2
        3, 3, 3, 3 -> 2

        """

        while l < r:
            if maxLeft > maxRight:
                r -= 1
                maxRight = max(maxRight, height[r])
                result += maxRight - height[r]
            else:
                l += 1
                maxLeft = max(maxLeft, height[l])
                result += maxLeft - height[l]
        
        return result





        
# input: array -> heights of each bar(wall)
# output: int -> maximum amount of water we can store

# example
# [1, 7, 2, 5] -> 10
# [] -> 0
# [1] -> 0
# [1, 4] -> 1

# info
# amount = min(height[l], height[r]) * (l - r)

# 2 pointer 
# initialize left pointer to start and right pointer to end
# initialize result to 0
# calculate area from both pointers
# move whichever pointer is the lower value
# recalculate area
# go until our pointers cross


# TC: O(n)
# SC: O(1)

"""
[1,7,2,5]

result, left, right
0, 0, 3


"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            result = max(result, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return result



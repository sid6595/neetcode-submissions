# input: array of heights
# output: maximum amount of water we can store

# approach
# 2 pointers, one at each end
# calculate the maximum water 
# what is our condition to shrink? 
# shrink from the minimum pointer

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        seen_max = 0

        while l < r:
            bound = min(heights[l], heights[r])

            cur = (r - l) * bound
            seen_max = max(seen_max, cur)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return seen_max
        
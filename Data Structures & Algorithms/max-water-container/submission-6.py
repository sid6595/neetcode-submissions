class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_seen = 0

        l, r = 0, len(heights) - 1

        while l < r:
            constraint = min(heights[l], heights[r])
            max_seen = max(max_seen, constraint * (r-l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_seen

# [2, 1, 100, 1, 1, 2]

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1

        current_best = 0

        while L < R:
            amount = (R - L) * min(heights[R], heights[L])

            if amount > current_best:
                current_best = amount
            
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return current_best
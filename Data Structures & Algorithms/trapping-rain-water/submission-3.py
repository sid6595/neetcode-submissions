class Solution:
    def trap(self, height: List[int]) -> int:
        left_boundary, right_boundary = height[0], height[-1]
        total = 0

        l, r = 0, len(height) - 1
        while l < r:
            left_h, right_h = height[l], height[r]

            if height[l] < height[r]:
                total += max(0, left_boundary - height[l])
                left_boundary = max(left_boundary, height[l])
                l += 1
            else:
                total += max(0, right_boundary - height[r])
                right_boundary = max(right_boundary, height[r])
                r -= 1
        
        return total
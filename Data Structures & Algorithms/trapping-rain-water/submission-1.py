# given: array of non-negative ints 
# output: int -> maximum area of water trapped between bars

"""

xxxx
xx
x
x
xx
xxx


"""

# 2 pointer



class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1

        leftmax, rightmax = height[L], height[R]
        
        result = 0

        while L < R:
            if leftmax < rightmax:
                L += 1
                leftmax = max(leftmax, height[L])
                result += leftmax - height[L]
            else:
                R -= 1 
                rightmax = max(rightmax, height[R])
                result += rightmax - height[R]
        
        return result






        
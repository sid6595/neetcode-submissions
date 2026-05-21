

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search through end of rows
        # binary search through individual row

        # matrix[i] is each row

        L, R = 0, len(matrix) - 1
        row = -1

        if target <= matrix[0][-1]:
                R = L
                row = 0
        # get correct row
        while L != R:
            mid = (R + L) // 2
            if R - L == 1:
                L = R
                row = R
            elif matrix[mid][-1] < target:
                L = mid
            elif matrix[mid][-1] >= target:
                R = mid
        
        #print(row)

        if row == -1:
            return False
            
        # search individual row
        L, R = 0, len(matrix[0]) - 1

     
        while L <= R:
            mid = (R + L) // 2
            print(mid)
            if matrix[row][mid] < target:
                L = mid + 1
            elif matrix[row][mid] > target:
                R = mid - 1
            else:
                return True
        
        return False


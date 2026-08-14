class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        directions = [(1,0), (0,1)] # down or right

        ROWS, COLS = len(grid), len(grid[0])

        # only positive numbers? 
        # can we revisit cells? -> not possible anyway

        visited = {}

        def dfs(row, col):
            if row == ROWS - 1 and col == COLS - 1:
                return grid[row][col]
            
            if row == ROWS or col == COLS:
                return float('inf') # out of bounds
            
            if (row, col) in visited:
                return visited[row, col] # we already know the result
            
            res = float('inf')
            
            for rc, cc in directions:
                new_row, new_col = row + rc, col + cc
                res = min(res, dfs(new_row, new_col))
            
            res += grid[row][col]
            visited[row, col] = res
            return res
        
        return dfs(0, 0)
        
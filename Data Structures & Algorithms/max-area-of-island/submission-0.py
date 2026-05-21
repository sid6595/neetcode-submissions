

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        visited = set()
        cur_max = 0

        def dfs(row, column):
            # base cases
            # check if this node is a zero
            # check if this node is inbounds
            # check if this node is visited
            if (min(row, column) < 0 or row >= ROWS or column >= COLUMNS or
                    (row, column) in visited or grid[row][column] == 0):
                return 0
            
            cur_length = 1
            visited.add((row,column))
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in directions:
                row_add, column_add = direction
                new_row, new_column = row + row_add, column + column_add
                cur_length += dfs(new_row, new_column)
            
            return cur_length     

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    cur_max = max(cur_max, dfs(i, j))
        
        return cur_max

        
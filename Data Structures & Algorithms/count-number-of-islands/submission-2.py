# 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        islands = []
        visited = set()

        def dfs(row, col, current_island):
            if min(row,col) < 0 or row >= ROWS or col >= COLS or (row,col) in visited or grid[row][col] == '0':
                return
                
            current_island.append([row,col])
            visited.add((row,col))

            for rc, cc in directions:
                new_row, new_col = row + rc, col + cc
                dfs(new_row, new_col, current_island)
            
            

        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == '1':
                    islands.append(dfs(i, j, []))
        
        return len(islands)

                
        
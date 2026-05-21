# loop through each row and column
# traverse from each unvisited cell = 1
# keep track of maximum
# return maximum

# can traverse through either bfs or dfs
# let's do dfs

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        max_seen = 0
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLUMNS
                or (r,c) in visited or grid[r][c] != 1):
                return 0
            
            visited.add((r,c))
            return 1 + (sum(dfs(r + dr, c + dc) for dr, dc in directions))

        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 1 and (row,col) not in visited:
                    island_size = dfs(row, col)
                    max_seen = max(max_seen, island_size)
        
        return max_seen

        


        
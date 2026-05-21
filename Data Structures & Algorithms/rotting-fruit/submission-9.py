class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]

        starting_rotten = []
        minutes_elapsed = 0
        fresh_fruit_count = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    starting_rotten.append((row,col))
                if grid[row][col] == 1:
                    fresh_fruit_count += 1
        
        queue = deque(starting_rotten)

        while queue and fresh_fruit_count > 0:
            minutes_elapsed += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                for rc, cc in directions:
                    nr, nc = row + rc, col + cc
                    if (nr >= 0 and nc >=0 and nr < ROWS and nc < COLS 
                        and grid[nr][nc] == 1):
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh_fruit_count -= 1
            

        
        return minutes_elapsed if fresh_fruit_count == 0 else -1
        
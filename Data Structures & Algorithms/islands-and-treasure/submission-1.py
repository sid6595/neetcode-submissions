class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        distance = 0

        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] == 0:
                    queue.append((row,column))
                    visited.add((row,column))
        
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                grid[row][col] = distance

                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for direction in directions:
                    row_shift, col_shift = direction
                    new_row, new_col = row + row_shift, col + col_shift

                    if (min(new_row, new_col) < 0 or new_row >= ROWS or new_col >= COLUMNS 
                        or (new_row,new_col) in visited or grid[new_row][new_col] == -1):
                        continue
                    
                    queue.append((new_row,new_col))
                    visited.add((new_row,new_col))
            distance += 1
        

        
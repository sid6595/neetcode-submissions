# input: nxn binary matrix
# output: length of shortest path

# path: top left to bottom right
# all visited cells are 0
# can traverse 8 directions, can move diagonally

# bfs

# initialize our visited set, queue
# add the initial top-left cell to the queue

# base cases, edge cases
# return -1 if top left is 1

# as we are performing bfs check:
# cell is within the bounds of the grid (upper and lower)
# cell is not previously visited

# return when we've reached bottom left
# keep incrementing our length as we proceed through the queue

# TC: O(n*m) -> only visit each node once
# SC: O(n*m)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        
        if grid[0][0] == 1:
            return -1
        
        visited = set()
        queue = deque()
        queue.append((0,0))

        length = 1
        
        while queue:
            for i in range(len(queue)):
                row, column = queue.popleft()
                print(row, column)

                if row == ROWS - 1 and column == COLUMNS - 1:
                    return length
                
                directions = [(-1, -1), (-1, 0), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
                for row_add, column_add in directions:
                    new_row, new_col = row + row_add, column + column_add
                    if min(new_row, new_col) < 0 or max(new_row, new_col) >= ROWS or (new_row, new_col) in visited or grid[new_row][new_col] == 1:
                        continue
                    
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
            length += 1

        return -1



        
        
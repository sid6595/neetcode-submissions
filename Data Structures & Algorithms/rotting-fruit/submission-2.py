# given: 2d matrix -> each cell is empty, fresh, rotten
# output: int -> minimum minutes until there are no fresh fruit (1)

# info
# 0, 1, 2
# every minute a 1 is 4-directionally adjacent to a 2, it becomes a 1
# what happens to empty cells? -> nothing
# how many rotten fruit can we start with -> no limit
# do we start at minute 0 -> yes
# unit by unit

# algo -> bfs
# traverse minute by minute
# initialize a queue, initialize a set of visited cells
# pass all current rotten fruits into the queue

# base cases
# if we go out of bounds
# if we go to an already rotten fruit (2)
# if we go to an empty cell (0)

# make our current fruit rotten

# once we exit bfs, re-check the grid
# if there are any 1s, return -1
# else, return our time

# TC: [checking grid for initial 2s] O(n^2) + [BFS] O(n^2) + [checking grid for remaining 1s] O(n^2)
# SC: [max length of queue, visited] O(n^2)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        # initialize
        queue = deque()
        visited = set()
        minute = 0

        # go through grid for rotten fruits
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    queue.append((row,column))
                    visited.add((row,column))
        
        if queue:
            minute -= 1
        
        while queue:
            for i in range(len(queue)):              
                # pop a fruit fruit
                row, column = queue.popleft()

                # turn it rotten b/c it's in queue
                grid[row][column] = 2

                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for direction in directions:
                    add_row, add_column = direction
                    new_row, new_column = row + add_row, column + add_column

                    if (min(new_row, new_column) < 0 or new_row >= ROWS or new_column >= COLUMNS 
                        or (new_row, new_column) in visited or grid[new_row][new_column] == 0):
                        continue
                    
                    queue.append((new_row, new_column))
                    visited.add((new_row, new_column))
            # each level of the bfs is a minute passed
            minute += 1
        
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    return -1
        
        return minute
        







        
        
# input
# m x n grid
# each value is either: -1 (no go), 0 (treasure), inf (traversable)

# output
# m x n grid
# each land value should be modified to the distance to nearest treasure chest
# if no treasure is reachable, remain inf

# info
# grid is 4-directional traversal
# possible to have unreachable land values
# reset queue/visited for each node
# perform BFS one at a time

# nearest path = BFS
# initialize queue
# initialize visited nodes
# keep track of distance traveled

# TC: O(n * (n*m)) = O(n^2 * m)
# SC: O(n*m)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None

        ROWS, COLUMNS = len(grid), len(grid[0])
        INF = 2147483647

        # bfs
        def bfs(row, col):
            queue = deque()
            visited = set()

            queue.append((row, col))

            length = 0

            while queue:
                for i in range(len(queue)):
                    # base cases
                    # check if inbounds, check if visited, check if -1
                    new_row, new_col = queue.popleft()

                    # can make more efficient by removing visited
                    # altering each as we go
                    # backtracking with dfs
                    if (min(new_row, new_col) < 0 or new_row >= ROWS or new_col >= COLUMNS
                        or (new_row, new_col) in visited or grid[new_row][new_col] == -1):
                        continue

                    if grid[new_row][new_col] == 0:
                        return length
                    
                    visited.add((new_row,new_col))

                    directions = [(0,1), (0,-1), (1,0), (-1,0)]
                    for direction in directions:
                        row_add, column_add = direction
                        bn_row, bn_col = new_row + row_add, new_col + column_add
                        queue.append((bn_row, bn_col))
                length += 1
            return INF

        
        # go through entire grid looking for land
        for row_val in range(ROWS):
            for col_val in range(COLUMNS):
                if grid[row_val][col_val] == INF:
                    grid[row_val][col_val] = bfs(row_val, col_val)

        
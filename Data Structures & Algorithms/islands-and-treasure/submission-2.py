# is it better to run bfs from each land cell to the closest treasure chest
# or from each treasure chest to all land cells and take the minimum

# approach 1
# TC: O(m*n * [number of land cells])

# approach 2
# TC: O(m*n * [number of treasure cells])

# let's go with option 1, a little simpler since there's no minimums to deal with
# we iterate through the grid
# if we come across an infinite value, run bfs from that cell

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def bfs(row, col):
            queue = deque()
            queue.append((row,col))

            distance = 0
            seen = set()

            while queue:
                for i in range(len(queue)):
                    cur_row, cur_col = queue.popleft()

                    if grid[cur_row][cur_col] == 0:
                        grid[row][col] = distance
                        return
                    
                    seen.add((cur_row, cur_col))

                    for rc, cc in directions:
                        new_row, new_col = cur_row + rc, cur_col + cc
                        if (new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS 
                            or (new_row, new_col) in seen or grid[new_row][new_col] == -1):
                            continue
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col))
                distance += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2147483647:
                    bfs(row,col)

            


        
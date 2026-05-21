class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        pac_vis = [[False] * COLUMNS for _ in range(ROWS)]
        atl_vis = [[False] * COLUMNS for _ in range(ROWS)]

        def bfs(source, visited):
            queue = deque(source)
            while queue:
                row, col = queue.popleft()
                visited[row][col] = True

                for row_add, column_add in directions:
                    new_row, new_col = row + row_add, col + column_add
                    if(min(new_row, new_col) < 0 or new_row >= ROWS or new_col >= COLUMNS
                        or visited[new_row][new_col] or heights[new_row][new_col] < heights[row][col]):
                        continue
                    queue.append((new_row,new_col))

        atl = []
        pac = []

        for row in range(ROWS):
            for col in range(COLUMNS):
                if row == 0 or col == 0:
                    pac.append((row,col))
                if row == ROWS-1 or col == COLUMNS-1:
                    atl.append((row,col))
        
        bfs(atl, atl_vis)
        bfs(pac, pac_vis)

        result = []
        for row in range(ROWS):
            for col in range(COLUMNS):
                if pac_vis[row][col] and atl_vis[row][col]:
                    result.append([row, col])

        return result



        
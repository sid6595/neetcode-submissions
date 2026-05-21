class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        pac_seen = [[0] * COLS for row in range(ROWS)]
        atl_seen = [[0] * COLS for row in range(ROWS)]

        def traversal(row, col, ocean):
            ocean[row][col] = 1

            for rc, cc in directions:
                new_row, new_col = row + rc, col + cc
                if (min(new_row, new_col) < 0 or new_row >= ROWS or new_col >= COLS 
                    or ocean[new_row][new_col] == 1 or heights[new_row][new_col] < heights[row][col]):
                    continue
                traversal(new_row, new_col, ocean)
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    traversal(i, j, pac_seen)
                if i == ROWS - 1 or j == COLS - 1:
                    traversal(i, j, atl_seen)
        
        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if atl_seen[i][j] and pac_seen[i][j]:
                    res.append([i,j])
        
        return res

                    


            
        
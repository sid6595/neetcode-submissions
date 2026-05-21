class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        atl_visited, pac_visited = set(), set()

        def dfs(row, column, visited, prev_height):
            if (min(row, column) < 0 or row >= ROWS or column >= COLUMNS 
                or (row,column) in visited or heights[row][column] < prev_height):
                return
            
            visited.add((row,column))
            for row_add, column_add in directions:
                new_row, new_column = row + row_add, column + column_add
                dfs(new_row, new_column, visited, heights[row][column])
            
        for row in range(ROWS):
            for column in range(COLUMNS):
                if row == 0 or column == 0:
                    dfs(row, column, pac_visited, 0)
                if row == ROWS - 1 or column == COLUMNS - 1:
                    dfs(row, column, atl_visited, 0)
        
        results = []
        for row in range(ROWS):
            for column in range(COLUMNS):
                if (row,column) in atl_visited and (row,column) in pac_visited:
                    results.append([row,column])
        
        return results


        
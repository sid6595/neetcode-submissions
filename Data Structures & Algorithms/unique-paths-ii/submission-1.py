# input: grid
# obstacle -> 1, space -> 0
# cannot traverse an obstacle square

# output: NUMBER OF POSSIBLE UNIQUE PATHS

# approach: dfs traversal
# no need for a visited set since we are allowed to go to the same cell
# will always be unique since we can only go down or right

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        directions = [(1,0), (0, 1)] # can move down and can move right
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])

        # check if we start in a obstacle -> no solutions
        if obstacleGrid[0][0] == 1:
            return 0
        
        seen = {}

        def dfs(row, col):
            # want to do a post order traversal
            # call dfs on all neighbors recursively
            # return the final result

            # check if invalid
            if row == ROW or col == COL or obstacleGrid[row][col] == 1:
                return 0

            # check if success
            if row == ROW-1 and col == COL-1:
                return 1

            if (row, col) in seen:
                return seen[(row, col)]
            
            unique_paths = 0

            for rc, cc in directions:
                new_row, new_col = row + rc, col + cc
                unique_paths += dfs(new_row, new_col)
            
            seen[row, col] = unique_paths

            return unique_paths

        return dfs(0, 0)
        

        
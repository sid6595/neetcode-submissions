# all paths -> DFS
# m is the number of rows, n is cols

# treat this as a graph
# neighbors

# remember everything is 1-indexed, need to sub 1
# no need for a visited set since it's not possible to go back to a previous state

# TC: O(V * E) -> O(m^2 * n^2)
# SC: O(m + n)
import functools

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROW_LEN = m
        COL_LEN = n


        @functools.lru_cache(None)

        def dfs(row, col):
            # check if row and col are within bounds
            if row == ROW_LEN or col == COL_LEN:
                return 0
            
            # termination state
            if row == ROW_LEN - 1 and col == COL_LEN - 1:
                return 1
            
            return dfs(row+1, col) + dfs(row, col+1)

        return dfs(0,0)

        

        


        
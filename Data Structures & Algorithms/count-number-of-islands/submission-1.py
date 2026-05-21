# matrix graph

# input: grid (1 is land, 0 is water)
# output: int -> number of islands

# info
# island: any land fully surround by water
# the entire of the grid counts as water

# approach
# store a list of lists of our islands
# store all visited nodes
# each list will be the (row, column) units within an island
# traverse the entire grid
# when we hit a 1 that has not been visited, we will perform dfs

# dfs

# base cases
# check if we are inbounds (lower and upper)
# check if current node has been visited

# check all possible directions for 1s
# do this recursively
# if there are no 1s, we stop
# have created an island
# append to our islands array

# return the list of our islands array

# TC: O(n*m)
# SC: O(n*m)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = []
        visited = set()

        def dfs(row, column, cur_island):
            row = int(row)
            column = int(column)
            if (min(row, column) < 0 or (row >= len(grid)) 
            or (column >= len(grid[0])) or (row, column) in visited):
                return
            if grid[row][column] == "0":
                return
            
            cur_island.add((row, column))
            visited.add((row,column))

            dfs(row + 1, column, cur_island)
            dfs(row - 1, column, cur_island)
            dfs(row, column + 1, cur_island)
            dfs(row, column - 1, cur_island)

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1" and (row, column) not in visited:
                    print("run")
                    current_island = set()
                    dfs(row, column, current_island)
                    islands.append(current_island)
        
        
        
        print(islands)
        print(visited)
        return len(islands)
            
            


                


        
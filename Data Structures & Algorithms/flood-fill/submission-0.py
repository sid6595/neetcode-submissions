# given: m x n grid of integers -> image, 3 ints -> sr, sc, color
# output: perform a flood fill on image from image[sr][sc], return modified image

# flood fill
# change start pixel to color
# perform same process for all adjacent cells that share start color of starting pixel
# do this recursively
# stop when there are no more pixels to modify

# dfs
# start at our starting pixel

# base cases:
# check that we are in bounds (max or min)
# check that we haven't already modified a pixel -> can our color be the same color as the start pixel? 
# done? -> all adjacent cells are visited or not start color

# modify current cell
# if its same color as start cell, change its color to color

# append our current cell to visited cells
# perform dfs on all its adjacent cells

# return modified grid

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        start_color = image[sr][sc]

        def dfs(image, row, column, visited) -> List[List[int]]:
            if ((min(row, column) < 0) or (row >= len(image)) or (column >= len(image[0])) 
            or ((row, column) in visited)):
                return image
            
            if image[row][column] == start_color:
                image[row][column] = color
            # don't continue if we can't modify this
            else:
                return image
            
            visited.add((row,column))

            image = dfs(image, row + 1, column, visited)
            image = dfs(image, row - 1, column, visited)
            image = dfs(image, row, column + 1, visited)
            image = dfs(image, row, column - 1, visited)

            return image

        return dfs(image, sr, sc, visited)
        
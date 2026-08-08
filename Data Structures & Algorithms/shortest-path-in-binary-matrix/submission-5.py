class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        side = len(grid)

        if len(grid) == 0 or grid[0][0] == 1:
            return -1

        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        length = 0

        while queue:
            length += 1
            for i in range(len(queue)):
                coord = queue.popleft()
                if coord == ((side-1), (side-1)):
                    return length
                
                for y_ch, x_ch in directions:
                    new_y, new_x = coord[0] + y_ch, coord[1] + x_ch
                    if ((new_y, new_x) not in visited and new_y >= 0 and new_y < side and new_x >= 0
                     and new_x < side and grid[new_y][new_x] == 0):
                        queue.append((new_y, new_x))
                        visited.add((new_y, new_x))
        
        return -1



        
        
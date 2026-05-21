class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        if image[sr][sc] == color:
            return image
        else:
            start_color = image[sr][sc]

        queue = deque()
        queue.append((sr, sc))

        while queue:
            row, col = queue.popleft()
            image[row][col] = color

            for rc, cc in directions:
                new_row, new_col = row + rc, col + cc
                if min(new_row, new_col) < 0 or new_row >= ROWS or new_col >= COLS or image[new_row][new_col] != start_color:
                    continue
                queue.append((new_row, new_col))
        
        return image
        
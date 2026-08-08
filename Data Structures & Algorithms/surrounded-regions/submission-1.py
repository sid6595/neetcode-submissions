# input: m x n matrix board ('X', 'O')
# output: alter the input board

# key details
# regions can be any shape
# surrounded -> none of the 'O' are on edge / enclosed by 'X'
# being connected only matters 4 directionally

# questions
# limit of the size of the board? -> 10^2
# invalid inputs? -> no

# approach
# bfs style
# if x, we ignore
# if o, add to our queue, perform bfs
# store island positions within the bfs
# if we determine a region is 'surrounded', go back and change them all to x

# SC: O(n*m)
# TC: O(n*m)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        ROWS, COLUMNS = len(board), len(board[0])

        visited = set()

        def bfs(row, column):
            nonlocal visited
            queue = deque()
            queue.append((row, column))
            visited.add((row, column))
            res = []
            surrounded = True

            while queue:
                r, c = queue.popleft()
                res.append((r, c))

                if r == 0 or c == 0 or r == ROWS - 1 or c == COLUMNS - 1:
                    surrounded = False
                
                for rc, cc in directions:
                    nr, nc = r + rc, c + cc
                    if (nr >= 0 and nc >= 0 and nr < ROWS and nc < COLUMNS and (nr,nc) not in visited 
                        and board[nr][nc] == 'O'):
                        queue.append((nr,nc))
                        visited.add((nr,nc))

            if surrounded:
                    return res

            return []    
            
        for i in range(ROWS):
            for j in range(COLUMNS):
                if board[i][j] == 'O' and (i, j) not in visited:
                    to_modify = bfs(i, j)

                    for row, column in to_modify:
                        board[row][column] = 'X'


        
        
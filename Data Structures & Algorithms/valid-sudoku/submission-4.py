# approach

# 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        HEIGHT, WIDTH = len(board), len(board[0])

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].add(board[i][j])
                    
                    if board[i][j] in columns[j]:
                        return False
                    else:
                        columns[j].add(board[i][j])
                    
                    if board[i][j] in boxes[(i // 3) * 3 + (j // 3)]:
                        return False
                    else:
                        boxes[(i // 3) * 3 + (j // 3)].add(board[i][j])
        
        return True
                        

        
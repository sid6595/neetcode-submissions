class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        squares = defaultdict(list)

        for i in range(len(board)): #rows
            for j in range(len(board[0])): #columns
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i]
                    or board[i][j] in columns[j]
                    or board[i][j] in squares[i // 3, j // 3]):
                    return False

                rows[i].append(board[i][j])
                columns[j].append(board[i][j])
                squares[i // 3,j // 3].append(board[i][j])
        
        return True
                
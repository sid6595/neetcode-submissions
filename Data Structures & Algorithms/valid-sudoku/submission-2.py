# O (n^2)
# O (n^2)



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 #n
        columns = [0] * 9 #n
        squares = [0] * 9 #n
        # (i // 3) * 3 + (j // 3)

        for i in range(len(board)): #rows
            for j in range(len(board[0])): #columns
                if board[i][j] == ".":
                    continue
                
                bitwise = int(board[i][j]) - 1
                shifted = 1 << bitwise

                if (shifted) & rows[i]:
                    return False
                if (shifted) & columns[j]:
                    return False
                if (shifted) & squares[(i // 3) * 3 + (j // 3)]:
                    return False

                rows[i] |= shifted
                columns[j] |= shifted
                squares[(i // 3) * 3 + (j // 3)] |= shifted
        
        return True
                
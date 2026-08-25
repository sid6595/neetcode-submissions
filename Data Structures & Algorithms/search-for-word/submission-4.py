class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        ROW, COL = len(board), len(board[0])

        searched = set()

        def dfs(row, col, index):
            if board[row][col] != word[index]:
                return False
            
            searched.add((row, col))
            
            index += 1
            if index == len(word):
                return True

            for rc, cc in directions:
                new_row, new_col = row + rc, col + cc
                if (new_row >= 0 and new_row < ROW and new_col >= 0 and new_col < COL and
                    (new_row, new_col) not in searched and dfs(new_row, new_col, index)):
                    return True
            
            searched.remove((row, col))
            return False

        
        for i in range(ROW):
            for j in range(COL):
                if dfs(i, j, 0):
                    return True

        return False
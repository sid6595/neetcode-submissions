# key constraints
# each row, column, and square should be 1-9
# only thing to check for is repeats and out of bounds

# to flatten the 2d into 1d we can do (3 * (r // 3) + (c // 3))

# TC: O(r * c) - go through each cell once, this is technically O(1) since it's 9x9
# SC: O(9 * 9) - also O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9
        # create dictionary for each row, column, and square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # add each to each dictionary it belongs to
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])
                if val < 1 or val > 9:
                    return False
                # add to row
                if val in rows[i] or val in cols[j] or val in squares[3 * (i // 3) + (j // 3)]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                squares[3 * (i // 3) + (j // 3)].add(val)
        
        return True
        
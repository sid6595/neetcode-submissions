class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # m x n -> n x m
        # 2 x 4 -> 4 x 2

        
        # to rotate, swap x and y

        # each row is independent
        # can create the output for each row
        # put them together in reverse order at the end

        res_list = []

        for row in boxGrid:
            stack = []
            for o in row:
                if o == ".":
                    temp = []
                    while stack and stack[-1] == "#":
                        temp.append(stack.pop())
                    stack.append(o)
                    stack.extend(temp)
                else:
                    stack.append(o)
            res_list.append(stack)
        
        # [0,0] -> [0,1] (m, n) -> (n, len(m)-1-m)
        # [1,0] -> [0,0]
        # [0,1] -> [1,1]
        # [0, 3] -> [3, 1]
        # rotate result 90 degrees

        ROW, COL = len(boxGrid), len(boxGrid[0]) # 2 x 4

        final = [[0] * ROW for _ in range(COL)] # 4 x 2

        for m in range(COL): # 4 -> each row
            for n in range(ROW): # 2 -> each col
                final[m][ROW - n - 1] = res_list[n][m]
        
        return final

        
            
        
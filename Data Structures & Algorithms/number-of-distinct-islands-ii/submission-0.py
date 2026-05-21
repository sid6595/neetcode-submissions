class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])  # grid dimensions
        visited = set()  # track visited land cells
        shapes = set()  # store canonical shapes of islands

        def dfs(r, c, cells):
            # Bounds check, water check, visited check
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or grid[r][c] == 0 or (r, c) in visited):
                return
            visited.add((r, c))  # mark current cell visited
            cells.append((r, c))  # record cell in this island
            dfs(r + 1, c, cells)  # explore down
            dfs(r - 1, c, cells)  # explore up
            dfs(r, c + 1, cells)  # explore right
            dfs(r, c - 1, cells)  # explore left

        def canonical(cells):
            # Generate all 8 rotations/reflections
            transforms = [[] for _ in range(8)]
            for x, y in cells:
                transforms[0].append((x, y))       # identity
                transforms[1].append((x, -y))      # reflect y
                transforms[2].append((-x, y))      # reflect x
                transforms[3].append((-x, -y))     # 180 rotation
                transforms[4].append((y, x))       # diagonal reflect
                transforms[5].append((y, -x))      # rotation
                transforms[6].append((-y, x))      # rotation
                transforms[7].append((-y, -x))     # anti-diagonal reflect
            # Normalize each: sort, then shift so min is (0,0)
            normalized = []
            for t in transforms:
                t.sort()  # sort coords lexicographically
                ox, oy = t[0]  # min point to translate to origin
                normalized.append(tuple((x - ox, y - oy) for x, y in t))
            return min(normalized)  # pick lexicographically smallest as canonical key

        for r in range(rows):  # iterate all cells
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:  # new island
                    cells = []  # collect island cells
                    dfs(r, c, cells)  # flood fill
                    shapes.add(canonical(cells))  # add unique shape
        return len(shapes)  # number of distinct islands


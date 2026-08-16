class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        winning = sum(piles) // 2 + 1
        memo = {}

        def dfs(start, end, total):
            if total >= winning:
                return True
            
            if start == end:
                return False
            
            if (start, end, total) in memo:
                return memo[start, end, total]
            
            
            memo[start, end, total] = dfs(start + 1, end, total + piles[start]) or dfs(start, end - 1, total + piles[end - 1])

            return memo[start, end, total]
        
        start, end = 0, len(piles)
        return dfs(start, end, 0)

        
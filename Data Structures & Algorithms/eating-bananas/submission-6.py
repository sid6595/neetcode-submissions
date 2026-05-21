class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def possible(speed):
            time = 0

            for pile in piles:
                time += (pile + speed - 1) // speed
            
            if time <= h:
                return True
            
            return False
        
        while l < r:
            m = (l + r) // 2
            if possible(m):
                r = m
            else:
                l = m + 1
        
        return l
        
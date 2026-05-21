# given array of ints, piles
# given integer h
# piles[i] is # of bananas in ith pile
# h is the max number of hours to eat all bananas

# output, minimum bph k

# rules
# eat k bananas from a pile every hour
# only one pile per hour

# will we always have a solution -> yes
# will piles always contain elements -> yes
# can we eat from a pile 2 separate times -> yes

# info
# if h = len(piles) -> k must be max(piles)
# max(piles) is our upper bound 

# examples
# [1,4,3,2], 9 -> 2

# binary search
# search between the minimum value 1 and the maximum, max(piles)
# O(n)
# perform binary search on each of these values 
# n - number of elements, m - largest element
# O(n log m)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def simulate(rate):
            time = 0
            bound = h
            for pile in piles:
                time += (pile + rate - 1) // rate
            if time <= bound:
                return time
            return None
        
        while l < r:
            mid = (l + r) // 2
            if simulate(mid):
                r = mid
            else:
                l = mid + 1
        
        return l



        
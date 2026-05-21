# given: array of UNSORTED intervals
# output: number of intervals we need to remove to make everything NON OVERLAPPING

# example
# [1,2] [2,4] [1,4] -> [1,2] [2,4] -> 1

# key info
# non-overlapping means we can have an equal start and end point
# we still need to sort
# we'll always remove the largest endpoint

# approach
# sort intervals by start point
# if we have overlapping intervals, keep the one that ends earliest

# TC: O(n log n)
# SC: O(n)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        min_endpoint = None
        res = 0

        """
        [1,4] [1,2] [2,4]

        4
        res = 1, 2

        """
        for start, end in intervals:
            if not min_endpoint:
                min_endpoint = end
                continue
            
            if start < min_endpoint:
                res += 1
                min_endpoint = min(min_endpoint, end)
            else:
                min_endpoint = end
        
        return res
        
# input: array of intervals
# contain the start and end points of those intervals

# output: array of non-overlapping intervals

# key info
# order does not matter

# example
# [1,3] [1, 5] -> [1, 5]

# approach
# sort the intervals
# compare end_i to end_i+1
# if end_1+1 <= end_i, we merge


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        prev = None
        res = []

        for start, end in intervals:
            if not prev:
                prev = [start, end]
                continue

            if start <= prev[1]:
                prev[1] = max(prev[1], end)
            else:
                res.append(prev)
                prev = [start, end]
        
        if prev:
            res.append(prev)
        
        return res
            

        
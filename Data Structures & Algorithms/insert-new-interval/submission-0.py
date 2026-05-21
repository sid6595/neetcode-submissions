# input
# array of NON-OVERLAPPING intervals
# sorted by start_i in ASCENDING ORDER
# given a new interval which can overlap

# output
# array of NON-OVERLAPPING intervals
# with new interval added in

# example
# [1,3] [4,6] ; [2,5] -> [1,6]
# [2,3] -> [0,4] -> [0,4]

# keep in mind
# new interval could be new start or end point
# all positive? -> yes
# new interval can contain more than 1 of previous intervals

# approach: sorted line
# store a dictionary of all start and end points as keys
# include intervals + new interval
# increment each start and decrement each end
# sort this dictionary by keys

# store seen for whether we close our interval
# if it's 0, we add current interval to our output
# current interval
# result set

# TC: O(n log n)
# SC: O(n)

"""
[1,3] [4,6] , [2,5]

{}
{1: 1, 3: -1, 4: 1, 6: -1, 2: 1, 5: -1}
{1: 1, 2: 1, 3: -1, 4: 1, 5: -1, 6: -1}

[1], [], 

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals_dict = defaultdict(int)

        for start, end in intervals:
            intervals_dict[start] += 1
            intervals_dict[end] -= 1

        intervals_dict[newInterval[0]] += 1
        intervals_dict[newInterval[1]] -= 1
        
        seen = 0
        current_interval, res = [], []

        """
        {1: 1, 2: 1, 3: -1, 4: 1, 5: -1, 6: -1}

        key = 1, [1], seen = 1
        key = 2, [1], seen = 2
        key = 3, [1], seen = 1
        key = 4, [1], seen = 2
        key = 5, [1], seen = 1
        key = 6, [1], seen = 0, [1, 6], [[1,6]], []

        """

        for key in sorted(intervals_dict):
            if not current_interval:
                current_interval.append(key)
            
            seen += intervals_dict[key]

            if seen == 0:
                current_interval.append(key)
                res.append(current_interval)
                current_interval = []
        
        return res
        
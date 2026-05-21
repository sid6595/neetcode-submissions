"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# given: start and end times of meetings
# output: whether we can attend them all or not

# sort the intervals by start time
# traverse in order
# if at any point, a value is less than the value before, return false

class Solution:

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        prev_end = 0

        for interval in intervals:
            start, end = interval.start, interval.end
            if start < prev_end:
                return False
            prev_end = end
        
        return True



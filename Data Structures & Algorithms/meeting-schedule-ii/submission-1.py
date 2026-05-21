"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#approach
#order by start times
#if an end time is after the next start time, add one to number of rooms needed
#keep 2 variables: total rooms and rooms occupied
#if both are equal, add 1 to total rooms

# TC
# to sort -> O (n log n)
# to 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x.start)

        total_rooms = 0
        rooms_occupied = 0

        past_meetings = []
        heapq.heapify(past_meetings)

        for interval in intervals:
            while past_meetings and past_meetings[0] <= interval.start:
                rooms_occupied -= 1
                heapq.heappop(past_meetings)
            
            rooms_occupied += 1
            heapq.heappush(past_meetings, interval.end)

            total_rooms = max(total_rooms, rooms_occupied)
        
        return total_rooms

        
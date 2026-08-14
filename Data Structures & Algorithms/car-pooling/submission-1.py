# if numPassengers[i] > capacity -> False
# valid inputs? -> yes
# will inputs be sorted in any way? 

# 1 2 3 4
# var = curCapacity  


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key = lambda x: x[1]) # O(n log n)

        cur_passengers = 0
        end_time_heap = []

        for i in range(len(trips)):
            numPassengers, start_pos, end_pos = sorted_trips[i]

            while end_time_heap and start_pos >= end_time_heap[0][0]:
                prev_end_time, passengers_leaving = heapq.heappop(end_time_heap)
                cur_passengers -= passengers_leaving
            
            cur_passengers += numPassengers
            if cur_passengers > capacity:
                return False
            
            heapq.heappush(end_time_heap, (end_pos, numPassengers))
        
        return True

            
        
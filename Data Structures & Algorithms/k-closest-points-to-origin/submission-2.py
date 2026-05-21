

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, [x, y]))  # max heap

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for (_, point) in heap]
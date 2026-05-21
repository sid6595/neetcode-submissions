class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0
        
        stone_heap = [-s for s in stones]
        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            greatest = heapq.heappop(stone_heap)
            second = heapq.heappop(stone_heap)

            # -5, -4
            if second > greatest:
                heapq.heappush(stone_heap, greatest-second)
        
        if stone_heap:
            return -1 * heapq.heappop(stone_heap)
        else:
            return 0

        
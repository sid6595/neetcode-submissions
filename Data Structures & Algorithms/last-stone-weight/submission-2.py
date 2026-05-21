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
        
        stone_heap.append(0)
        return -stone_heap[0]


        
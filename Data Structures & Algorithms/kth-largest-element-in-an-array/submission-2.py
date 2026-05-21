class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result_heap = []
        heapq.heapify(result_heap)

        for num in nums:
            heapq.heappush(result_heap, num)
            if len(result_heap) > k:
                heapq.heappop(result_heap)
        
        return heapq.heappop(result_heap)
        
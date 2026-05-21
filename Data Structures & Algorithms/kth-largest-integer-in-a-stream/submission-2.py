# input: stream of unsorted integers, k
# output: the kth largest integer 

# key points
# stream can contain duplicates



class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create a min heap of k values

        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        

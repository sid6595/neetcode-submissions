# given: unsorted array of integers, int k
# output: kth largest element in the array

# heap create a binary tree
# kth largest
# max heap, pop k times (kth largest)
# min heap, pop (length of integer - k + 1) times, (kth largest)

# [1,2,3]
# 1 largest
# min heap (1,2,3) -> 1, 2, (3)
# max heap (3,2,1) -> (3)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        result = -1

        # (0-2)
        for i in range(len(nums) - k + 1):
            result = heapq.heappop(nums)
        
        return result
        
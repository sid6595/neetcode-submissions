# given: array of ints, target integer
# output: the total number of subarrays equaling k

# example
# [2, -1, 1, 2] , 2 -> [2], [2, -1, 1], [-1, 1, 2], [2] -> 4
# [4,4,4,4,4,4] , 4 -> 6

# key info
# subarray is contiguous, consecutive digits

# prefix sum
# 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = -k
        res = 0
        freq = {0:1}

        for num in nums:
            cur += num
            if cur in freq:
                res += freq.get(cur, 0)
            freq[cur + k] = freq.get(cur + k, 0) + 1
            
        return res

        
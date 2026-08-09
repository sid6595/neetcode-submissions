class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        maxSeen, minSeen = arrays[0][-1], arrays[0][0]
        res = 0

        for i in range(1, len(arrays)):
            array = arrays[i]
            res = max(res, abs(array[0] - maxSeen), abs(array[-1] - minSeen))
            print(maxSeen, minSeen)
            maxSeen = max(maxSeen, array[-1])
            minSeen = min(minSeen, array[0])
        
        return res
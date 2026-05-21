# create 2 dictionaries
# the keys are the frequency
# one dictionary contains the location
# the other contains the frequency
# at the end we output elements in descending order of what frequencies exist

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = defaultdict(set)
        location_table = defaultdict(int)
        res = []

        for num in nums:
            location_table[num] += 1
            position = location_table[num]
            if position > 1:
                frequency_table[position-1].remove(num)
            frequency_table[position].add(num)

        for i in range(max(location_table.values()), -1, -1):
            for num in frequency_table[i]:
                if len(res) == k:
                    return res
                res.append(num)
        
        return res



        
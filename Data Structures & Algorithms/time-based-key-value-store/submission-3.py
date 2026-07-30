class TimeMap:

    def __init__(self):
        # object of data structure
        # each value has a list of timestamps
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # stores key with value at timestamp
        key_timestamps = self.time_map[key]
        # push values as a heap
        # will have ordered timestamps
        pair = (value, timestamp)

        key_timestamps.append(pair)
        

    def get(self, key: str, timestamp: int) -> str:
        # returns the previous timestamp that key was called at before the input timestamp
        # return "" if no such value exists
        # when we are pulling previous timestamps, we can binary search since they are sorted

        all_timestamps = self.time_map[key]

        res = ""
        
        # binary search on all timestamps
        l, r = 0, len(all_timestamps) - 1
        while l <= r:
            mid = (l + r) // 2

            if all_timestamps[mid][1] <= timestamp:
                res = all_timestamps[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
        

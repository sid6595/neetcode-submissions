class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # store character, frequency, and last position
        
        seen_count = defaultdict(int)
        distinct_seen = 0

        l = 0
        res = 0

        for r in range(len(s)):
            seen_count[s[r]] += 1

            if seen_count[s[r]] == 1:
                distinct_seen += 1

            while distinct_seen > k:
                seen_count[s[l]] -= 1
                if seen_count[s[l]] == 0:
                    distinct_seen -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res

        
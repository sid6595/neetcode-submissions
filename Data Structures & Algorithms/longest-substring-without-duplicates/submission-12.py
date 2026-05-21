class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = 0
        seen_chars = defaultdict(int)

        result = 0

        l = 0

        for r in range(len(s)):
            seen_chars[s[r]] += 1
            while seen_chars[s[r]] > 1:
                seen_chars[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        
        return result
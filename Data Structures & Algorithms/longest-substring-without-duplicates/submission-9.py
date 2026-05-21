class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        L = 0
        curMax = 0

        """
        z, x, y, z

        [z]

        """

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            curMax = max(curMax, R - L + 1)
        
        return curMax
        
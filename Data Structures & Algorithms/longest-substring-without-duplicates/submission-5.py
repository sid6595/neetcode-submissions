class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, best = 0, 0

        seen = set()

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
                
            
            best = max(best, R - L + 1)
            seen.add(s[R])
            
        
        return best

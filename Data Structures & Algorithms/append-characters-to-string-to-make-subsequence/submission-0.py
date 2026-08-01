#2 pointer
#one pointer at s, one pointer at t
# increment pointer when we see the correct character in t
# however many characters remain is the solution

# TC: O(n) where n is the length of s
# SC: O(1) we are only storing the pointers

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0

        while l < len(s):
            if s[l] == t[r]:
                r += 1
                if r == len(t):
                    return 0
            l += 1
        
        return len(t) - r
        
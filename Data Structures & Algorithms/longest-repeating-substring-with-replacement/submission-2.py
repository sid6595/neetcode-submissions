# input: string of UPPERCASE characters, integer k

# output: replace up to k characters of string with a character
# return the length of longest possible substring with 1 character

# examples
# "XYYX" , 2 -> 4
# "", 5 -> 0
# "ABCCB", 2 -> 4
# "ABCA", 2 -> 4

# info
# empty string always returns 0

# approach
# sliding window
# keep track of frequency of each character we've seen
# keep track of the max frequency
# we're good until the max frequency + k > len of our substring
# once that happens we move our window

# "AAABCDEF", 1 -> 4

# TC: O(n)
# SC: O(1)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        l = 0
        max_freq = 0
        char_seen = defaultdict(int)
        res = 0

        """
        X,Y,Y,X , k = 2

        {X: 1}, 1, 3 < 1, no loop, 1
        {X: 1, Y: 1}, 1, 3 < 2, no loop, 2
        {X: 1, Y: 2}, 2, 4 < 3, no loop, 3
        {X: 2, Y: 2}, 2, 4 < 4, no loop, 4 
        """
        for r in range(len(s)):
            char_seen[s[r]] += 1
            max_freq = max(max_freq, char_seen[s[r]])
            while max_freq + k < (r - l + 1):
                char_seen[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        
        return res
            
        

        
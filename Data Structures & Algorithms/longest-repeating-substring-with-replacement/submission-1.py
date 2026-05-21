# input: string -> uppercase characters, int -> k
# output: int -> length of longest substring with only 1 character after k replacements

# additional info
# only have uppercase characters
# is k always < len(string) -> yes

# sliding window
# initialize left and right pointers, both at the start
# initialize a dictionary of each seen character and their frequency
# initialize maxFreq, res

# example
# [XYYX] -> 4

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        seen = defaultdict(int)
        maxFreq, res = 0, 0

        for r in range(len(s)):
            seen[s[r]] += 1
            maxFreq = max(maxFreq, seen[s[r]])

            while (r - l + 1) > maxFreq + k:
                seen[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

        
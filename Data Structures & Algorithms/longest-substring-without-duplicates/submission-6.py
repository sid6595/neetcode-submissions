# input s -> string
# goal: length of longest substring without duplicates

# cases
# ["zxyz"] -> 3
# [""] -> 0
# ["Aab"] -> 3

# set 2 pointers, L and R
# move R and keep adding to our set of seen characters
# keep updating our 'best' value
# once we hit a seen character, move L pointer one over
# go until R gets to the end of s
# return bpest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, best = 0, 0

        seen = set()


        """
        pwwkew
        pweknwdsd

        R, L, seen, best
        0, 0, (), 0
        0, 0, (p), 1
        1, 0, (p, w), 2
        2, 1, (p, w), 2
        3, 1, (p, w, k), 3



        """
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            best = max(best, R - L + 1)

        return best

        
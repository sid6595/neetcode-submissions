class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 2 pointers
        # increment right pointer, add new character to dict
        # if that character hasn't been seen, also increment a chars seen var

        # as soon as we see a third character, the left pointer should snap to the position of the next new char
        
        l, r = 0, 0
        seen_chars = defaultdict(int)
        while r < len(s):
            cur = s[r]
            first = s[l]
            seen_chars[cur] += 1
            if len(seen_chars) > 2:
                seen_chars[first] -= 1
                if seen_chars[first] == 0:
                    seen_chars.pop(first)
                l += 1
            r += 1
        
        return r - l
        
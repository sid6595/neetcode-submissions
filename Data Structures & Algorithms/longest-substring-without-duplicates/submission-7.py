# given: string
# output: string -> longest substring without duplicate characters

# examples
# "" -> 0
# zyx -> 3
# xxxxx -> 1
# zyxz -> 3
# abba -> 2

# approach
# initialize our 2 pointers to both be at the start of our string
# initialize a set of 'seen' characters
# initialize a result int = 0
# move the right pointer and check if the new character is in seen
# if yes -> move the left pointer and remove the character from our set
# keep going until the character at our right pointer is no longer at seen
# if no -> add new character to our set compare l-r to the result, take the max
# go until right pointer is greater len(input)
# return result

# TC: O(n)
# SC: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # initialize variables
        l, r = 0, 0
        seen = set()
        result = 0

        """
        xxxx 
        (), 0, 0, 0
        (x), 1, 0, 1
        (x), 1, 1, 2
        (x), 1, 2, 3
        (x), 1, 3, 4

        abba
        seen, result, left, right
        (), 0, 0, 0
        (a), 1, 0, 1
        (a,b), 2, 0, 2
        (b), 2, 2, 3
        (b, a), 2, 2, 4
        """
        # loop through our string
        while r < len(s):
            # check if the new character is in our substring
            while s[r] in seen:
                # remove characters until the new character is no longer in the substring
                seen.remove(s[l])
                l += 1
            # add new right character to set
            seen.add(s[r])
            # take the length of current substring and compare to our previous best
            result = max(result, r - l + 1)
            # move right pointer
            r += 1
        
        return result
        

        
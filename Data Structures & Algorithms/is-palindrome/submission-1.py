# palindrome, focus on characters
# case insensitive, all lowercase comps
# ignore non numbers/letters

# cases 
# ??race??car
# Racecar
# 400??4

# strip out all white space
# initialize pointers
# compare left and right

# TC: O(n)
# SC: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        
        return True
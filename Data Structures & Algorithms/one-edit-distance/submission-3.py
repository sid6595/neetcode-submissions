# given: strings s and t
# output: true if one edit distance apart, false otherwise

# edit distance
# s + [1 character] = t
# s - [1 character] = t
# s [replace 1 character] = t

# example
# s = "ab", t = "acb" -> adding 1 character -> True
# s = "abcd", t = "dcba" -> False
# s = "", t = "" -> False

# key info
# s = len(t) or s = len(t) + 1 or s = len(t) - 1
# all lowercase? 
# what characters are possible? numbers? 

# approach
# 

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t) - 2 or len(s) > len(t) + 2:
            return False
        
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)


        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i+1:]
        
        
        return len(s) + 1 == len(t)
        


        
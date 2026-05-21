# given: strings s and t
# output: shortest substring s so every character in t is present

# example
# s = "OUZODYXAZV", t = "XYZ" -> "YXAZ"
# s = "x", t = "xy" -> ""

# edge cases
# if t is longer than s, there is no solution

# naiive solution
# create a dictionary storing all characters in t
# check all substrings of s if they contain that dictionary

# sliding window solution
# create a dictionary for characters in t
# when we run into a character in t, decrement the dictionary
# when we have a value hit 0, increase our solution counter
# if our solution counter is equal to len(t), start reducing the size of window

# TC: o(n) where n is the len(s)
# SC: O(n), will store dictionary of t characters

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_chars = defaultdict(int)

        for char in t:
            t_chars[char] += 1
        
        l = 0
        matching = 0
        goal_matching = len(t_chars)

        result = ""
        result_len = len(s) + 1

        for r in range(len(s)):
            target_char = s[r]

            if target_char in t_chars:
                t_chars[target_char] -= 1
                if t_chars[target_char] == 0:
                    matching += 1
            
            while matching == goal_matching:
                # check if s[l] is in t
                if r - l + 1 < result_len:
                    result = s[l:r+1]
                    result_len = r - l + 1
                
                if s[l] in t_chars:
                    t_chars[s[l]] += 1
                    if t_chars[s[l]] > 0:
                        matching -= 1
                
                l += 1
        
        return result


        

        
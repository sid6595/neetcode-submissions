# ascii uses ord

class Solution:
    def scoreOfString(self, s: str) -> int:

        running_diff = 0
        prev_val = ord(s[0])

        for i in range(1,len(s)):
            current_val = ord(s[i])
            running_diff += abs(current_val - prev_val)
            prev_val = current_val
        
        return running_diff
        
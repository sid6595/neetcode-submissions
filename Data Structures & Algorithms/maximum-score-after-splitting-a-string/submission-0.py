# input: string of 0s and 1s
# output: maximum score

# score = # of 0s in left substring + # of 1's in right substring

# key info
# substrings must be non-empty

# example
# 011101 -> 0, 11101 -> 1 + 4 = 5
# 010101 -> 010, 101 -> 2 + 2 = 4
# 0110000 -> 011000, 0-> 4 + 0 = 4

# prefix sums
# calculate the prefix sum of 0s and postfix sum of 1s at each position
# loop through and get the maximum sum 

# define sum at index 0
# 0 at index 0, 1 at index 1-max

# define sum at index len(s) - 1
# not allowed out of bounds
# define sum at index len(s) - 2
# 0 at index len(s) - 2, 1 at index len(s) - 1

class Solution:
    
    def maxScore(self, s: str) -> int:
        prefix_sums = [0] * (len(s) - 1)
        postfix_sums = [0] * (len(s) - 1)

        zero_count = 0
        one_count = 0

        result = 0

        for index in range(len(s) - 1):
            if s[index] == '0':
                zero_count += 1
                prefix_sums[index] = zero_count
        
        for index in range(len(s) - 2, -1, -1):
            if s[index + 1] == '1':
                one_count += 1
                postfix_sums[index] = one_count
        
        for i in range(len(prefix_sums)):
            result = max(result, prefix_sums[i] + postfix_sums[i])
        
        return result



        
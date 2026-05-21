# given: array -> temperatures
# each index represents the temperature on that day

# output: array -> result
# each index represents the number of days from that day until we see a warmer temperature

# info
# last element will always be 0 in result set

# example
# [10, 20, 30] -> [1, 1, 0]
# [] -> []
# [30, 10, 20, 20] -> [0, 1, 0, 0]

# approach
# stack
# add each temperature and its index to the stack
# when we add new elements, compare to the top element
# if its greater, pop from stack and check the difference between indices
# thats what we populate our result array with
# do this until the end 
# if there are any elements remaining in the stack, their result is 0

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize stack
        seen_temps = []

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while seen_temps and seen_temps[-1][1] < temperatures[i]:
                prev_index, prev_temp = seen_temps.pop()
                result[prev_index] = i - prev_index
            seen_temps.append((i, temperatures[i]))
        
        return result





        
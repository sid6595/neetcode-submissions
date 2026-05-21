
"""
[30, 27, 28, 38]

[]
[1, 30]
[0, 30, 1, 27]
[]




"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1]:
                # popping stuff
                value = stack.pop()
                position = stack.pop()

                result[position] = i - position

            else:
                # position
                stack.append(i)
                # value
                stack.append(temperatures[i])
        
        return result

# can only have same type of bracket
# valid only if they close each other
# can't have different type of bracket in between

# cases
# empty -> true
# {, [, ], } -> true
# {,[,},] -> false
# ],[ -> false

# create a stack
# push elements until we see a close bracket
# once we do, pop once, then pop again
# if the second pop is the open bracket, keep going, if not return false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"}": "{", "]": "[", ")": "("}

        for element in s:
            stack.append(element)
            if element in map:
                closed = stack.pop()
                if len(stack) == 0:
                    return False
                if stack.pop() != map[closed]:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        
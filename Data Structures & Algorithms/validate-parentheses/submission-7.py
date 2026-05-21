# add each element to stack
# when we see a close element, pop 2 from stack
# confirm second pop is the open element, false if not
# keep going until stack is empty

# example
# [] -> true
# [']'] -> false
# ( [ [ ] ] ) -> true

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        element_key = {']': '[', '}': '{', ')': '('}
        stack = []

        for char in s:
            stack.append(char)
            if char in element_key:
                stack.pop()
                if not stack:
                    return False
                if stack.pop() != element_key[char]:
                    return False
        if not stack:
            return True
        else:
            return False


        
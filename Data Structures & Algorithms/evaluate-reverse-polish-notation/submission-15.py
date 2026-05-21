class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ('+', '-', '*', '/')

        stack = []

        for token in tokens:
            if token in operators:
                if len(stack) < 2:
                    return -1
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    stack.append(a+b)
                if token == '-':
                    stack.append(b-a)
                if token == '*':
                    stack.append(a*b)
                if token == '/':
                    stack.append(int(b/a))
            else:
                stack.append(int(token))
        
        return stack.pop()
        
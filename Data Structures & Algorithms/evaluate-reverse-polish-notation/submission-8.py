class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")

        if len(tokens) == 0:
            return 0
        
        
        for i in range(len(tokens)):
            print(stack)
            if tokens[i] in operators:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    stack.append(a+b)
                if tokens[i] == "-":
                    stack.append(b-a)
                if tokens[i] == "*":
                    stack.append(a*b)
                if tokens[i] == "/":
                    # [4, 2, /]
                    stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

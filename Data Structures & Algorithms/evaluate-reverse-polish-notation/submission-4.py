class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','/','*']
        stack = []
        res = 0
        for i in tokens:
            if i in operators:

                if i == '+':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a+b)
                if i == '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                if i == '*':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a*b)
                if i == '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
            else:
                stack.append(int(i))
        return stack[-1]
                
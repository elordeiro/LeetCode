class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '-':
                y = stack.pop()
                x = stack.pop()
                stack.append(x - y)
            elif token == '/':
                y = stack.pop()
                x = stack.pop()
                stack.append(int(float(x) / y))
            else:
                stack.append(int(token))
        
        return stack.pop()









if __name__ == "__main__":
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # tokens = ["4","-2","/","2","-3","-","-"]
    # tokens = ["2","1","+","3","*"]
    print(sol.evalRPN(tokens))
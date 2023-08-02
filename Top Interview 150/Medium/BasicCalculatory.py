class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        output, curr, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                curr = (curr * 10) + int(c)
            elif c in "+-":
                output += curr * sign
                curr = 0
                if c == '+':
                    sign = 1
                else:
                    sign = -1
            elif c ==   '(':
                stack.append(output)
                stack.append(sign)
                sign = 1
                output = 0
            elif c == ')':
                output += curr * sign
                output *= stack.pop()
                output += stack.pop()
                curr = 0
            
        return output + (curr * sign)




if __name__ == "__main__":
    sol = Solution()
    # s = "0"
    s = "2147483647"
    s = "1-11"
    s = "(1+(4+5+2)-3)+(6+8)"
    s = "1-(     -2)"
    print(sol.calculate(s))
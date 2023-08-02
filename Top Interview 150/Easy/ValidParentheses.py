class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
                continue
            if len(stack) == 0:
                return False
            top = stack.pop()
            if top == '{' and char != '}':
                return False
            if top == '[' and char != ']':
                return False
            if top == '(' and char != ')':
                return False
        
        if len(stack) == 0:
            return True
        
        return False

if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}("
    print(sol.isValid(s))
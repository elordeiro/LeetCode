class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['$']
        for char in s:
            curr = stack.pop()
            if curr == char:
                continue
            else:
                stack.append(curr)
                stack.append(char)
        
        stack = stack[1:]
        str = ""
        for char in stack:
            str += char
        return str





if __name__ == "__main__":
    sol = Solution()
    s = "azxxzy"
    # s = "abbaca"
    print(sol.removeDuplicates(s))
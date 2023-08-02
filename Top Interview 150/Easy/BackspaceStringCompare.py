class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        string1 = []
        string2 = []

        for char in s:
            if char == '#' and len(string1):
                string1.pop()
            elif char != '#':
                string1.append(char)
        
        for char in t:
            if char == '#' and len(string2):
                string2.pop()
            elif char != '#':
                string2.append(char)
        
        return string1 == string2

if __name__ == "__main__":
    sol = Solution()
    s = "a##c"
    t = "#a#c"
    print(sol.backspaceCompare(s, t))
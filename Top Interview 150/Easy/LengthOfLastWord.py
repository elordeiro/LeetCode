class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])

if __name__ =="__main__":
    sol = Solution()
    s = "Hello World"
    print(sol.lengthOfLastWord(s))
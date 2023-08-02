class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        i = 0
        for char in t:
            if i == n:
                return True
            if char == s[i]:
                i += 1
        if i == n:
            return True
        return False



if __name__ == "__main__":
    sol = Solution()
    s = ""
    t = "ahbgdc"
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1 and not s2 and s3:
            return False
        
        visited = set()
        stack = []
        while s3:
            char = s3[-1]
            if s1 and s2 and s1[-1] == s2[-1]:
                if (s1, s2, s3) not in visited:
                    stack.append((s1, s2, s3))
                    visited.add((s1, s2, s3))
            if s1 and char == s1[-1]:
                s1 = s1[:-1]
            elif s2 and char == s2[-1]:
                s2 = s2[:-1]
            else:
                if not stack:
                    return False
                s2, s1, s3 = stack.pop()
                continue
            s3 = s3[:-1]
        
        return True if not s1 and not s2 else False


if __name__ == "__main__":
    sol = Solution()
    s1, s2, s3 = "", "", "a" # False
    s1, s2, s3 = "a", "", "aa" # False
    s1, s2, s3 = "", "", "" # True
    s1, s2, s3 = "a", "b", "a" # False
    s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac" # True
    s1, s2, s3 = "aabc", "abad", "aabadabc" # True
    s1, s2, s3 = "aabcc", "dbbca", "aadbbbaccc" # False
    s1, s2, s3 = "", "b", "b" # True
    s1, s2, s3 = "db", "b", "cbb" # True
    print(sol.isInterleave(s1, s2, s3))
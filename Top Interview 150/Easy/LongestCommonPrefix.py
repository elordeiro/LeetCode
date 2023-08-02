class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                try:
                    if strs[0][i] == strs[j][i]:
                        continue
                    else:
                        return prefix
                except:
                    return prefix
            else:
                prefix += strs[0][i]
        
        return prefix

if __name__ == "__main__":
    sol = Solution()
    strs = ["dog","racecar","car"]
    strs = ["flower","flow","flight"]
    strs = ["ab","a"]
    print(sol.longestCommonPrefix(strs))
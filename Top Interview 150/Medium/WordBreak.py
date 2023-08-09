class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wordDict = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        longest = max(map(len, wordDict)) 

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - longest -1, -1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


        



if __name__ == "__main__":
    sol = Solution()
    s, wordDict = "aaaaaaa", ["aaaa","aaa"]
    s, wordDict = "bb", ["a","b","bbb","bbbb"]
    s, wordDict = "catsandog", ["cats","dog","sand","and","cat"]
    s, wordDict = "abcd", ["a","abc","b","cd"]
    s, wordDict = "leetcode", ["leet","code"]
    s, wordDict = "bccdbacdbdacddabbaaaadababadad", ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
    s, wordDict = "applepenapple", ["apple","pen"]
    print(sol.wordBreak(s, wordDict))
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    tests =  [
              ("horse", "ros", 3),
              ("", "a", 1),
              ("ab", "a", 1),
              ("park", "spake", 3),
              ("intention", "execution", 5),
              ("ab", "bc", 2),
              ("dinitrophenylhydrazine", "dimethylhydraz, ", 10),
            ]
    res = []
    failed = []
    ok = True
    for i, test in enumerate(tests, start=1):
        word1, word2, expected = test
        actual = sol.minDistance(word1, word2)
        res.append((expected, actual))
        if expected != actual:
            ok = False
            failed.append((i, expected, actual))
    if ok:
        print("Passed All Tests")
    else:
        print("Failed Tests:")
        for fail in failed:
            test_num, expected, actual = fail
            print(f"Test Number: {test_num}, Expected: {expected}, Actual: {actual}")
        print()
    print(res)
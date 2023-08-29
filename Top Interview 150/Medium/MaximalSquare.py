class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        biggest = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
                biggest = max(biggest, dp[i][j])
        return biggest ** 2


if __name__ == "__main__":
    sol = Solution()
    tests =  [
            #   ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
            #   ([["0","1"],["1","0"]], 1),
            #   ([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]], 4),
              ([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]], 9),
             ]
    res = []
    failed = []
    ok = True
    for i, test in enumerate(tests, start=1):
        matrix, expected = test
        output = sol.maximalSquare(matrix)
        res.append((output, expected))
        if output != expected:
            ok = False
            failed.append((i, output, expected))
    if ok:
        print("Passed All Tests")
    else:
        print("Failed Tests:")
        for fail in failed:
            test_num, output, expected = fail
            print(f"Test Number: {test_num}, Output: {output}, Expected: {expected}")
        print()
    print(res)
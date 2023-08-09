class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        memo = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        memo[m - 1][n] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                memo[i][j] = grid[i][j] + min(memo[i + 1][j], memo[i][j + 1])
        
        return memo[0][0]


if __name__ == "__main__":
    sol = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]] # 7
    grid = [[1,2,3],[4,5,6]]         # 12
    print(sol.minPathSum(grid))
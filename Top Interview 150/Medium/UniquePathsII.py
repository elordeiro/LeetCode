class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        memo[m - 1][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    memo[i][j] = memo[i + 1][j] + memo[i][j + 1]
        
        return memo[0][0]








if __name__ == "__main__":
    sol = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    obstacleGrid = [[0,1],[0,0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
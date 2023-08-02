class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        inslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    inslands += 1
                    self.BFS(grid, i, j, m, n)
        return inslands

    def BFS(self, grid, i, j, m, n):
        if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == '1':
            grid[i][j] = '#'
            self.BFS(grid, i+1, j, m, n)
            self.BFS(grid, i-1, j, m, n)
            self.BFS(grid, i, j+1, m, n)
            self.BFS(grid, i, j-1, m, n)


if __name__ == "__main__":
    sol = Solution()
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    print(sol.numIslands(grid))
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        self.visited = set()
        
        # Left Border
        # Right Border
        for i in range(m):
            if board[i][0] == 'O':
                self.BFS(board, i, 0, m, n)
            if board[i][n-1] == 'O':
                self.BFS(board, i, n-1, m, n)
            self.visited.add((i, 0))
            self.visited.add((i, n-1))
        
        # Top Border
        # Bottom Border
        for j in range(n):
            if board[0][j] == 'O':
                self.BFS(board, 0, j, m, n)
            if board[m-1][j] == 'O':
                self.BFS(board, m-1, j, m, n)
            self.visited.add((0, j))
            self.visited.add((m-1, j))

        for i in range(m):
            for j in range(n):
                if (i, j) not in self.visited:
                    board[i][j] = 'X'


    def BFS(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if (i, j) not in self.visited:
            self.visited.add((i, j))
            if grid[i][j] == 'O':
                self.BFS(grid, i-1, j, m, n)
                self.BFS(grid, i+1, j, m, n)
                self.BFS(grid, i, j-1, m, n)
                self.BFS(grid, i, j+1, m, n)


if __name__ == "__main__":
    sol = Solution()
    grid = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
           ]
    grid = [["O","O","O"],["O","O","O"],["O","O","O"]]
    sol.solve(grid)
    print(grid)
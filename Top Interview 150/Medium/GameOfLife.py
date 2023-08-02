import copy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        temp_board = copy.deepcopy(board)
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                count = self.countNeighbors(board, i, j, m, n)
                if board[i][j] == 1:
                    if count != 2 and count != 3:
                        temp_board[i][j] = 0
                else:
                    if count == 3:
                        temp_board[i][j] = 1
        
        for i in range(m):
            for j in range(n):
                board[i][j] = temp_board[i][j]
                


    def countNeighbors(self, board, row, col, m, n):
        #         l      r      u     d      ul      ur    dl    dr
        dirs = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        count = 0
        for r, c in dirs:
            i = row + r
            j = col + c
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] == 1:
                    count += 1
        return count

                






if __name__ == "__main__":
    sol = Solution()
    board = [[0,1,0],
             [0,0,1],
             [1,1,1],
             [0,0,0]]
    
    sol.gameOfLife(board)
    print(board)
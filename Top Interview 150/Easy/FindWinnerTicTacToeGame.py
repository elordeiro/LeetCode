class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]
        
        for i, move in enumerate(moves):
            x, y = move
            if i % 2 == 0:
                board[x][y] = 'A'
            else:
                board[x][y] = 'B'
        
        for row in board:
            if row[0] != '' and row[0] == row[1] and row[0] == row[2]:
                return row[0]
        
        for i in range(3):
            if board[0][i] != '' and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                return board[0][i]
        
        if board[0][0] != '' and board[0][0] == board[1][1] and board [0][0] == board[2][2]:
            return board[0][0]
        
        if board[0][2] != '' and board[0][2] == board[1][1] and board [0][2] == board[2][0]:
            return board[0][2]

        if len(moves) == 9:
            return 'Draw'
        
        return 'Pending'
    
if __name__ == "__main__":
    sol = Solution()
    moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    print(sol.tictactoe(moves))
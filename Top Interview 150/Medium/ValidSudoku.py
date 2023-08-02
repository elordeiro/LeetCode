class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp_row = []
        for row in board:
            for cell in row:
                if cell in temp_row:
                    return False
                if cell != '.':
                    temp_row.append(cell)
            temp_row = []

        sqrs = {}
        sqr_count = 1
        temp_col = []
        for j in range(9):
            if j % 3 == 0 and j > 0:
                sqr_count += 3
            for i in range(9):
                cell = board[i][j]
                if cell != '.':
                    if cell in temp_col:
                        return False 
                    sqr_num = sqr_count + (i // 3) 
                    if sqr_num not in sqrs:
                        sqrs[sqr_num] = [cell]
                    else:
                        if cell in sqrs[sqr_num]:
                            return False
                        sqrs[sqr_num].append(cell)
                    temp_col.append(cell)
            temp_col = []
        
        return True
        

if __name__ == "__main__":
    sol = Solution()
    board = [
                [".",".","5",   ".",".",".",   ".",".","6"],
                [".",".",".",   ".","1","4",   ".",".","."],
                [".",".",".",   ".",".",".",   ".",".","."],

                [".",".",".",   ".",".","9",   "2",".","."],
                ["5",".",".",   ".",".","2",   ".",".","."],
                [".",".",".",   ".",".",".",   ".","3","."],

                [".",".",".",   "5","4",".",   ".",".","."],
                ["3",".",".",   ".",".",".",   "4","2","."],
                [".",".",".",   "2","7",".",   "6",".","."]
            ]
    print(sol.isValidSudoku(board))
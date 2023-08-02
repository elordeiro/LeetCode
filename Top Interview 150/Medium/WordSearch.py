class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def backTrack(i, j, idx):
            if idx == word_len:
                return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx]:
                return False
            
            tmp, board[i][j] = board[i][j], '#'
            for k, l in dirs:
                if backTrack(i + k, j + l, idx + 1):
                    return True
            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backTrack(i, j, 0):
                    return True

        return False

if __name__ == "__main__":
    sol = Solution()
    board = [["a","a","b","a","a","b"],["b","a","b","a","b","b"],["b","a","b","b","b","b"],["a","a","b","a","b","a"],["b","b","a","a","a","b"],["b","b","b","a","b","a"]]
    word = "aaaababab"
    print(sol.exist(board, word))
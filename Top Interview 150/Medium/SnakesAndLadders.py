class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        nn = n ** 2
        
        dist = [-1] * nn
        dist[0] = 0
        
        squares = [board[i][j] - 1 for i in range(n - 1, -1, -1) 
                    for j in (range(n - 1, -1, -1) if (n - i) % 2 == 0 else range(n))]
        
        q = [0]
        while q:
            curr = q.pop(0)
            for i in range(curr+1, min(curr+7, nn)):
                destination = squares[i]
                if destination == -2:
                    destination = i
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        return dist[nn-1]




if __name__ == "__main__":
    sol = Solution()
    board = [[-1,-1,-1],[-1,9,8],[-1,8,9]] # 1
    board = [[-1,-1],[-1,3]] # 1
    board = [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]] # 2
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]] # 4
    board = [[1,1,-1],[1,1,1],[-1,1,1]] # -1
    board = [[-1,4,-1],[6,2,6],[-1,3,-1]] # 2
    print(sol.snakesAndLadders(board))
import copy

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        temp = copy.deepcopy(matrix)
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        temp[k][j] = 0
                    for l in range(n):
                        temp[i][l] = 0
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]




if __name__ == "__main__":
    sol = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(matrix)
    print(matrix)
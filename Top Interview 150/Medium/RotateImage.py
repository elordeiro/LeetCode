class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp = [list(x) for x in zip(*matrix[::-1])]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    sol.rotate(matrix)
    print(matrix)
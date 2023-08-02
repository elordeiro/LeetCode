class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        def findCell(row, left, right):
            if right < left:
                return False
            mid = left + ((right - left) // 2)
            mid_cell = matrix[row][mid]
            if target == mid_cell:
                return True
            elif target < mid_cell:
                return findCell(row, left, mid - 1)
            elif target > mid_cell:  
                return findCell(row, mid + 1, right)

        def findRow(up, down):
            if down < up:
                return False
            mid = up + ((down - up) // 2)
            first_cell = matrix[mid][0]
            last_cell = matrix[mid][n]
            if target < first_cell:
                return findRow(up, mid - 1)
            elif target > last_cell:
                return findRow(mid + 1, down)
            elif first_cell <= target <= last_cell:
                return findCell(mid, 0, n)

        return findRow(0, m)

        





if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 34
    print(sol.searchMatrix(matrix, target))
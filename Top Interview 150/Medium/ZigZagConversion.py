class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        two_d_array = [[''] * n for _ in range(numRows)]
        
        direction = -1
        i, j, k = 0, 0, 0
        while k < n:
            two_d_array[i][j] = s[k]
            if k % (numRows - 1) == 0:
                direction *= -1
            i += 1 * direction
            if direction == -1:
                j += 1
            k += 1
        
        string = ""
        for row in two_d_array:
            for char in row:
                if char != "":
                    string += char
        return string


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows))
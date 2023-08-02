class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqrt = 1
        while True:
            if sqrt * sqrt > x:
                return sqrt - 1
            sqrt += 1

        return sqrt


"""
25
110001
000101
"""
if __name__ == "__main__":
    sol = Solution()
    x = 25
    print(sol.mySqrt(x))
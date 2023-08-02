class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        total = 1
        if n > 0:
            for _ in range(n):
                total *= x
        else:
            for _ in range(-n):
                total /= x
        
        return total


if __name__ == "__main__":
    sol = Solution()
    x = 0.00001
    n = 2147483647
    print(sol.myPow(x, n))
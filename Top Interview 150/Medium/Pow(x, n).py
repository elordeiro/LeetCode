class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        is_positive = True
        if n < 0:
            is_positive = False
            n = ~n+1
        
        result = 1
        while n > 0:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result if is_positive else 1 / result 


if __name__ == "__main__":
    sol = Solution()
    x = 2
    n = -2
    print(sol.myPow(x, n))
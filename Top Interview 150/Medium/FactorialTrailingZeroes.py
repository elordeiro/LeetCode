class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroes = 0
        while n > 0:
            zeroes += n // 5
            n //= 5
        return zeroes


if __name__ == "__main__":
    sol = Solution()
    n = 10000
    print(sol.trailingZeroes(n))
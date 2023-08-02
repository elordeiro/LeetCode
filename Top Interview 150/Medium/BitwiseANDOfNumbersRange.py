class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        while right > left:
            right &= right - 1
        return right 


if __name__ == "__main__":
    sol = Solution()
    left = 5
    right = 7
    left = 600_000_000
    right = 2_147_483_645
    print(sol.rangeBitwiseAnd(left, right))
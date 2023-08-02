class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count('1')


if __name__ == "__main__":
    sol = Solution()
    n = int('00000000000000000000000000001011', 2)
    # print(n)
    print(sol.hammingWeight(n))

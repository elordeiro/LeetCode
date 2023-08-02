class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = str(bin(n))
        num = num[len(num):1:-1]
        for _ in range(32 - len(num)):
            num += '0'
        return int(num, 2)


if __name__ == "__main__":
    sol = Solution()
    n = int('00000010100101000001111010011100', 2)
    print(sol.reverseBits(n))

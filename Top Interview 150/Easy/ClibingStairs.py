from itertools import permutations

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1 1 1 1 1
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ways = [-1] * (n + 1)
        ways[0], ways[1], ways [2] = 0, 1, 2
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n]



if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.climbStairs(n))
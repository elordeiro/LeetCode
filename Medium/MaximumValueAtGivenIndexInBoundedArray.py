class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        maxSum -= n
        
if __name__ == "__main__":
    sol = Solution()
    n = 8
    index = 7
    maxSum = 14
    print(sol.maxValue(n, index, maxSum))
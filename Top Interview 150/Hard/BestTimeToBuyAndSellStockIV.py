class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        buy = [float('inf')] * k
        sell = [0] * (k+1)

        for price in prices:
            for i in range(k):
                if price - sell[i-1] < buy[i]:
                    buy[i] = price - sell[i-1]
                if price - buy[i] > sell[i]:
                    sell[i] = price - buy[i]

        return sell[-2]


if __name__ == "__main__":
    sol = Solution()
    tests = [
              (2, [2,4,1], 2), 
              (2, [3,2,6,5,0,3], 7),
              (2, [3,3,5,0,0,3,1,4], 6),
             ]
    for test in tests:
        k, prices, expected = test
        result = sol.maxProfit(k, prices)
        if result != expected:
            print(f"Test Failed: \n    Prices:   {prices}\n    Result:   {result}\n    Expected: {expected}")
            break
    else:
        print("Passed All Tests :)")
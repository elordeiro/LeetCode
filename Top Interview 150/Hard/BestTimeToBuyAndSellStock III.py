class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        More concise than next option but the same logic, just a bit slower
        
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1  = min(buy1,  price)
            sell1 = max(sell1, price - buy1)
            buy2  = min(buy2,  price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2
        """

        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0

        for price in prices:
            if price < buy1:
                buy1 = price
            if price - buy1 > sell1:
                sell1 = price - buy1
            if price - sell1 < buy2:
                buy2  = price - sell1
            if price - buy2 > sell2:
                sell2 = price - buy2

        return sell2

if __name__ == "__main__":
    sol = Solution()
    tests = [
              ([3,3,5,0,0,3,1,4], 6), 
              ([2,1,4,5,2,9,7], 11),
              ([1,2,4,2,5,7,2,4,9,0,9], 17)
             ]
    for test in tests:
        prices, expected = test
        result = sol.maxProfit(prices)
        if result != expected:
            print(f"Test Failed: \n    Prices:   {prices}\n    Result:   {result}\n    Expected: {expected}")
            break
    else:
        print("Passed All Tests :)")
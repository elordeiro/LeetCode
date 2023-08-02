class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = float('inf')
        total_profit = 0

        for i in range(len(prices)):
            temp = prices[i]
            if temp < buy_price:
                buy_price = temp
            elif temp > buy_price:
                total_profit += temp - buy_price
                buy_price = temp
                

        return total_profit if total_profit > 0 else 0

if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))

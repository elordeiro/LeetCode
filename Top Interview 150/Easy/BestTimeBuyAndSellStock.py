class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = float('-inf')
        min = float('inf')
        
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > max_profit:
                max_profit = prices[i] - min
        
        return max_profit

if __name__ =="__main__":
    sol = Solution()
    prices = [2,1,2,1,0,1,2]
    prices = [2,1,4]
    prices = [2,4,1]
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
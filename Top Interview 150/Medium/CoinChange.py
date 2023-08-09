class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            memo[i] = min([memo[i - coin] + 1 for coin in coins if i - coin >= 0] + [memo[i]])

        return memo[amount] if memo[amount] != float('inf') else -1





if __name__ == "__main__":
    sol = Solution()
    coins, amount = [1],0          # 0
    coins, amount = [1,2,5], 11    # 3
    coins, amount = [2,5,10,1], 27 # 4
    coins, amount = [186,419,83,408], 6249 # 20
    coins, amount = [2], 3         # -1
    print(sol.coinChange(coins, amount))
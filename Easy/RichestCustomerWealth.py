import heapq

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = []

        for customer in accounts:
            heapq.heappush(wealth, sum(customer))

        heapq._heapify_max(wealth)
        return heapq.heappop(wealth)

if __name__ == "__main__":
    sol = Solution()
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    print(sol.maximumWealth(accounts))

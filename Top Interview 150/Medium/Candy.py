class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        res = [1] * n
        
        total = n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                total -= res[i]
                res[i] = res[i-1] + 1
                total += res[i]
        
        for i in range(n-1,0,-1):
            if ratings[i-1] > ratings[i]:
                total -= res[i-1]
                res[i-1] = max(res[i]+1, res[i-1])
                total += res[i-1]
        
        return total

#200010000

if __name__ == "__main__":
    sol = Solution()
    ratings = [1,0,2]
    print(sol.candy(ratings))
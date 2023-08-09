class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}

        def solve(w1, w2, steps):
            if len(w1) > len(word1):
                return 
            if w1 == w2:
                return steps
            for i in range(len(w1)):
                new_w1 = w1
                
                new_w1 = w1[:i + steps] + w2[min(i + steps, len(w2) - 1)] + w1[i + steps + 1:]
                replace = solve(new_w1, w2, steps + 1)
                
                new_w1 = w1
                new_w1 = w1[:i + steps] + w1[i + steps + 1:]
                delete = solve(new_w1, w2, steps + 1)

                new_w1 = w1
                new_w1 = w1[:i + steps] + w2[min(i + steps, len(w2) - 1)] + w1[i + steps:]
                insert  = solve(new_w1, w2, steps + 1)
                
                if w1 not in memo:
                    memo[w1] = min(replace, delete, insert)
                else:
                    memo[w1] = min(memo[w1], replace, delete, insert)
            return memo[w1]

        solve(word1, word2, 0)
        return memo[word1]




if __name__ == "__main__":
    sol = Solution()
    word1, word2 = "intention", "execution" # 5
    word1, word2 = "horse", "ros"           # 3
    print(sol.minDistance(word1, word2))
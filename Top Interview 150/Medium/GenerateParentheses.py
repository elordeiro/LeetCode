class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backTrack(open, close, partial_res):
            if open > n or close > open:
                return
            if close == n:
                res.append(partial_res[:])
                return
            partial_res += "("
            backTrack(open+1, close, partial_res)
            partial_res = partial_res[:-1]
            partial_res += ")"
            backTrack(open, close+1, partial_res)
        backTrack(0, 0, "")
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))
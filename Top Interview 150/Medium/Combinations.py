class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backTrack(start, k, partial_res):
            if k == 0:
                res.append(partial_res[:])
                return
            for x in range(start , n - k + 2):
                partial_res.append(x)
                backTrack(x + 1, k - 1, partial_res)
                partial_res.pop()
        backTrack(1, k, [])
        
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 4
    print(sol.combine(n, k))
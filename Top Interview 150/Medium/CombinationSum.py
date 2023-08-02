class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(candidates)
        def backTrack(i, total, partial_res):
            if total == target:
                res.append(partial_res[:])
                return
            if i >= n or total > target:
                return
            partial_res.append(candidates[i])
            backTrack(i, total+candidates[i], partial_res)
            partial_res.pop()
            backTrack(i+1, total, partial_res)
        backTrack(0, 0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    candidates = [3,2,8]
    target = 18
    print(sol.combinationSum(candidates, target))
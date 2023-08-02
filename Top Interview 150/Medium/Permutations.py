class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backTrack(nums, partial_res):
            if not nums:
                res.append(partial_res[:])
                return
            for i, num in enumerate(nums):
                partial_res.append(num)
                backTrack(nums[0:i]+nums[i+1:], partial_res)
                partial_res.pop()
        backTrack(nums, [])
        return res




if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))
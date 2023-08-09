class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        res = [0]* n
        for i in range(n):
            res[i] = max(nums[i] + res[i - 2], res[i - 1])

        return res[-1]



if __name__ == "__main__":
    sol = Solution()
    nums = [2,1,1,2]   # 4
    nums = [1,2,3,1]   # 4
    nums = [3] # 12
    nums = [2,7,9,3,1] # 12
    print(sol.rob(nums))
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndingHere = nums[0]
        maxSoFar = nums[0]
        nums.pop(0)
        for x in nums:
            maxEndingHere = max(maxEndingHere + x, x)
            maxSoFar = max(maxSoFar, maxEndingHere)
        
        return maxSoFar
        



if __name__ == "__main__":
    sol = Solution()
    nums = [5,-3,5,5]
    print(sol.maxSubArray(nums))
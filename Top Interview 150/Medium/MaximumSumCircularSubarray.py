class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndingHere, maxSofar, minEndingHere, minSoFar, total = 0, nums[0], 0, nums[0], 0
        for x in nums:
            maxEndingHere = max(maxEndingHere + x, x)
            maxSofar = max(maxSofar, maxEndingHere)
            minEndingHere = min(minEndingHere + x, x)
            minSoFar = min(minSoFar, minEndingHere)
            total += x

        return max(maxSofar, (total - minSoFar))  if maxSofar > 0 else maxSofar



if __name__ == "__main__":
    sol = Solution()
    nums = [5,-3,5]
    nums = [1,-2,3,-2]
    nums = [-3,-2,-3]
    print(sol.maxSubarraySumCircular(nums))
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum = sum ^ num
        return sum

if __name__ == "__main__":
    sol = Solution()
    nums = [4,1,2,1,2]
    print(sol.singleNumber(nums))
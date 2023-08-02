class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appears_once = 0
        appears_twice = 0

        for num in nums:
            appears_once = (appears_once ^ num) & (~appears_twice)
            appears_twice = (appears_twice ^ num) & (~appears_once)

        return appears_once

if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,3,2]
    nums = [1,1,1,2,2,2,122,5,5,5]
    nums = [0,1,0,99,1,0,1]
    print(sol.singleNumber(nums))
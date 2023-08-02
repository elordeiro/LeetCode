class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        nums = sorted(list(set(nums)))
        n = len(nums)
        streak = 1
        longest_streak = 0

        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                streak += 1
            else:
                if streak > longest_streak:
                    longest_streak = streak
                streak = 1
        return longest_streak if longest_streak > streak else streak


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0]
    print(sol.longestConsecutive(nums))
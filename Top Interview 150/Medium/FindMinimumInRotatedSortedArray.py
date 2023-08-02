class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(left, right):
            if nums[left] <= nums[right]:
                return nums[left]
            if left > right:
                return 5001
            mid = left + (right - left) // 2
            return min(nums[mid], binarySearch(left, mid -1), binarySearch(mid + 1, right))
        
        return binarySearch(0, len(nums) - 1)













if __name__ == "__main__":
    sol = Solution()
    nums = [3,1,2]
    print(sol.findMin(nums))
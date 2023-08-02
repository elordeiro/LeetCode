class Solution(object):
    def helperFunction(self, nums, target, left, right, index):
        if right < 0:
            return 0
        if left >= len(nums):
            return left
        if left > right:
            return index
        
        mid = ((right - left) // 2) + left
        current = nums[mid]
        if current == target:
            return mid
        if current > target:
            return self.helperFunction(nums, target, left, mid - 1, mid)
        return self.helperFunction(nums, target, mid + 1, right, mid + 1)
    


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.helperFunction(nums, target, 0, len(nums), 0)
        
    

if __name__ == "__main__":
    sol = Solution()
    # nums = [1,3,5,7,9]
    # target = 2
    nums = [1,3]
    target = 4
    print(sol.searchInsert(nums, target))
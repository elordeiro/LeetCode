class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        n = len(nums)
        while k > n:
            k = k - n
        temp = [nums[i] for i in range(n-1, n - k - 1, -1)]
        
        for i in range(n-1, k - 1, -1):
            nums[i] = nums[i-k]
        
        for i in range(len(temp)):
            nums[i] = temp.pop()

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(sol.rotate(nums, k))
    print(nums)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        left = 1
        for i in range(n):
            if i > 0:
                left = res[i-1] * nums[i-1]
            res[i] = left
        
        right = 1
        for i in range(n-1,-1,-1):
            if i < n - 1:
                right *= nums[i+1]
            res[i] *= right
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,1,0,-3,3]
    nums = [0,0]
    nums = [1,-1]
    nums = [9,0,-2]
    nums = [0,4,0]
    nums = [1,2,3,4]
    nums = [5,9,2,-9,-9,-7,-8,7,-9,10]
    print(sol.productExceptSelf(nums))
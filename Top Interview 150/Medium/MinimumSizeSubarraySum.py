class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i, j = 0, 0
        min_length = float('inf')
        sum = 0
        
        while j <= n:
            while sum >= target:
                if j - i < min_length:
                    min_length = j - i
                sum -= nums[i]
                i += 1
            try:
                sum += nums[j]
                j += 1
            except:
                break
                
        return min_length if min_length != float('inf') else 0


if __name__ == "__main__":
    sol = Solution()
    target = 11
    nums = [1,2,3,4,5]
    print(sol.minSubArrayLen(target, nums))
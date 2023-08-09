class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(nlog(n)) Solution
        """
        tails = []

        for num in nums:
            n = len(tails)
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == n:
                tails.append(num)
            else:
                tails[left] = num
        
        return len(tails)






if __name__ == "__main__":
    sol = Solution()
    nums = [7,7,7,7,7,7,7]
    nums = [10,9,2,5,3,7,101,18]
    nums = [0,1,0,3,2,3]
    print(sol.lengthOfLIS(nums))
    
    
    # O(n^2) Solution
    # n = len(nums)
    # memo = [1] * n

    # for i, num1 in enumerate(nums):
    #     for j, num2 in enumerate(nums[:i]):
    #         if num1 > num2 and memo[i] < memo[j] + 1:
    #             memo[i] = memo[j] + 1
    
    # return max(memo)
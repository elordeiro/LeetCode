class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        to_remove = False
        i, j = 0, 1
        while j < n:
            if nums[i] == nums[j] and not to_remove:
                to_remove = True
                j += 1
            elif nums[i] == nums[j] and to_remove:
                for k in range(j, n - 1):
                    nums[k] = nums[k + 1]
                n -= 1
            else:
                i = j
                j += 1
                to_remove = False
        return n
        

if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    print(sol.removeDuplicates(nums))
    print(nums)
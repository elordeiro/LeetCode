class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        last_open = len(nums) - 1
        i = 0
        count = 0
        while i <= last_open:
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[last_open]
                nums[last_open] = temp
                last_open -= 1
            else:
                count += 1
                i += 1
        return count
            
 
if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,2,3]
    val = 3
    print(sol.removeElement(nums, val))
    print(nums)

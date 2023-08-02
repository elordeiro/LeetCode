class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = []
        repeat_nums = []
        unique_nums.append(nums[0])
        
        for i in range(1, len(nums)):
            curr = unique_nums.pop()
            if curr == nums[i]:
                unique_nums.append(curr)
                repeat_nums.append(nums[i])
            else:
                unique_nums.append(curr)
                unique_nums.append(nums[i])
                

        k = len(unique_nums)
        for i in range(k):
            nums[i] = unique_nums[i]
        
        for i in range(k, len(repeat_nums)):
            nums[i] = repeat_nums[i]

        return k


if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(nums))
    print(nums)
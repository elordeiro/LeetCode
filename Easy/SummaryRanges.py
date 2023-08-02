class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        output = []
        start = nums[0]
        end = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                end = nums[i + 1]
            else:
                if start == end:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                start = nums[i + 1]
                end = nums[i + 1]
        
        if start == end:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))
        
        return output


if __name__ == "__main__":
    sol = Solution()
    nums = [0,2,3,4,6,8,9]
    # nums = [-1]
    # nums = [1, 3]
    print(sol.summaryRanges(nums))
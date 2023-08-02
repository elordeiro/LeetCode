class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        mjr_elmt = len(nums) // 2
        
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
            
            if dict[num] > mjr_elmt:
                    return num


if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,1,1,1,2,2]
    print(sol.majorityElement(nums))
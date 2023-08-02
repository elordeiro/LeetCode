class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                if i - dict[nums[i]] <= k:
                    return True
                else:
                    dict[nums[i]] = i
            else:
                dict[nums[i]] = i
        
        return False
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,1,1]
    k = 1
    print(sol.containsNearbyDuplicate(nums, k))
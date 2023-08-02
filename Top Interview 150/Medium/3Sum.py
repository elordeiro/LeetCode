class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        i, j, k= 0,0,0
        res = []
        while i < n:
            target = -nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    res.append(triplet)
                    while j < k and nums[j] == triplet[1]:
                        j += 1
                    while k > j and nums[k] == triplet[2]:
                        k -= 1
            while i + 1 < n and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return res
        


if __name__ == "__main__":
    sol = Solution()
    nums = [3,0,-2,-1,1,2]
    print(sol.threeSum(nums))
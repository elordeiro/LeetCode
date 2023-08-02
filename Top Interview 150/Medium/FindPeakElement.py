class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, float("-inf"))
        nums.append(float("-inf"))

        def binarySearch(left, right):
            if right == left:
                return left - 1
            
            mid = left + ((right - left) // 2)
            mid_element = nums[mid]
            
            if mid_element < nums[mid - 1]:
                return binarySearch(left, mid - 1)
            elif mid_element < nums[mid + 1]:
                return binarySearch(mid + 1, right)
            else:
                return mid - 1
        
        return binarySearch(1, n)

                


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.findPeakElement(nums))
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) - 1
        sol = [-1, -1]

        def findFirst(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                mid_el = nums[mid]
                if target < mid_el:
                    right = mid - 1
                elif target > mid_el:
                    left = mid + 1
                else:
                    sol[0] = mid
                    right = mid - 1

        def findLast(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                mid_el = nums[mid]
                if target < mid_el:
                    right = mid - 1
                elif target > mid_el:
                    left = mid + 1
                else:
                    sol[1] = mid
                    left = mid + 1

        findFirst(0, n)
        sol[0] != -1 and findLast(sol[0], n)

        return sol





if __name__ == "__main__":
    sol = Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(sol.searchRange(nums, target))
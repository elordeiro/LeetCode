class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        def findPivot(left, right):
            if nums[left] <= nums[right]:
                return 0
            if left == right - 1:
                return right
            mid = left + (right - left) // 2
            temp = findPivot(left, mid)
            if temp == 0:
                temp = findPivot(mid + 1, right)
                if temp == 0:
                    return mid + 1
                else:
                    return temp
            else:
                return temp
        pvt = findPivot(0, n - 1)

        nums = nums[pvt:] + nums[0:pvt]

        def search(left, right):
            if left > right:
                return - 1
            mid = left + (right - left) // 2
            mid_el = nums[mid]
            if target < mid_el:
                return search(left, mid - 1)
            elif target > mid_el:
                return search(mid + 1, right)
            else:
                return mid
        res = search(0, n - 1 )
        return (res + pvt) % n if res != -1 else -1




if __name__ == "__main__":
    sol = Solution()
    nums = [3,1]
    target = 3
    print(sol.search(nums, target))
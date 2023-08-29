import time

class Solution(object):
    def searchRange(self, nums, target):
        left  = 0
        right = len(nums) - 1
        start = -1

        while left <= right:
            mid = (left + right) >> 1
            mid_el = nums[mid]
            if target < mid_el:
                right = mid - 1
            elif target > mid_el:
                left = mid + 1
            else:
                start = mid
                right = mid - 1
        
        if start == -1:
            return [-1, -1]
        
        end = -1
        left = start
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            mid_el = nums[mid]
            if target < mid_el:
                right = mid - 1
            elif target > mid_el:
                left = mid + 1
            else:
                end = mid
                left = mid + 1
        
        return [start, end]






if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10]
    target = 10
    # nums = [0,1]
    # target = 1
    start_time = time.time()
    print(sol.searchRange(nums, target))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Runtime: {round(elapsed_time, 9)}s")



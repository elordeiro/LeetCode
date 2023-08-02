import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for x in nums:
            heapq.heappush(heap, -x)
        
        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)





if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(sol.findKthLargest(nums, k))
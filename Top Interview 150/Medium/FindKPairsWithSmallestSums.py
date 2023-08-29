import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        len1 = len(nums1)
        len2 = len(nums2)
        sol  = []
        heap = []
        i = 0
        while i < k and i < len1:
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
            i += 1
        
        while k > 0 and heap:
            k -= 1
            _, i, j = heapq.heappop(heap)
            sol.append((nums1[i], nums2[j]))
            
            j += 1
            if j < len2:
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
        
        return sol


if __name__ == "__main__":
    sol = Solution()
    # nums1, nums2, k = [1,1,2],  [1,2,3], 4
    # nums1, nums2, k = [1,7,11], [2,4,6], 3
    nums1, nums2, k = [1,2,4], [-1,1,2], 100
    print(sol.kSmallestPairs(nums1, nums2, k))
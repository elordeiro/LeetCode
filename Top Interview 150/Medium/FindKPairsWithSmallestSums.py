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
        sol = []
        heap= []
        visited = set()
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0,0))
        
        while len(sol) < k and heap:
            _, i, j = heapq.heappop(heap)
            sol.append((nums1[i], nums2[j]))

            if i + 1 < len1 and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j)) 
            
            if j + 1 < len2 and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1)) 

        return sol


if __name__ == "__main__":
    sol = Solution()
    # nums1, nums2, k = [1,1,2],  [1,2,3], 4
    # nums1, nums2, k = [1,7,11], [2,4,6], 3
    nums1, nums2, k = [1,2,4], [-1,1,2], 100
    print(sol.kSmallestPairs(nums1, nums2, k))
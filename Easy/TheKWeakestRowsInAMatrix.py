import heapq

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        minpq = []
        for i, row in enumerate(mat):
            count_ones = row.count(1)
            heapq.heappush(minpq, (count_ones, i))
        
        result = []
        for i in range(k):
            _, row = heapq.heappop(minpq)
            result.append(row)
        return result

if __name__ == "__main__":
    sol = Solution()
    mat = [[1,1,0,0,0],
           [1,1,1,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0],
           [1,1,1,1,1]]
    k = 3
    print(sol.kWeakestRows(mat, k))

from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        
        n = len(points)
        longest_line = 0

        for i in range(n):
            slope_map = {}
            for j in range(i + 1, n):
                (a, b), (c, d) = points[i], points[j]
                if a == c:
                    slope_map[float('inf')] = slope_map.get(float('inf'), 1) + 1
                elif b == d:
                    slope_map[0] = slope_map.get(0, 1) + 1
                else:
                    slope = (a - c) / (b - d)
                    slope_map[slope] = slope_map.get(slope, 1) + 1
            if slope_map:
                longest_line = max(max(slope_map.values()), longest_line)

        return longest_line


if __name__ == "__main__":
    sol = Solution()
    # points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    points = [[9,-25],[-4,1],[-1,5],[-7,7]]
    print(sol.maxPoints(points))
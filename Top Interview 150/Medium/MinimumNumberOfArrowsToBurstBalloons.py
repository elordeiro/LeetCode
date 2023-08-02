class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        points = sorted(points)

        start, end = points[0]
        arrows = 1
        for i in range(1, n):
            x, y = points[i]
            if start <= x <= end or start <= y <= end:
                start = max(start, x)
                end = min(end, y)
            else:
                arrows += 1
                start = x
                end = y
        
        return arrows














if __name__ == "__main__":
    sol = Solution()
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(sol.findMinArrowShots(points))
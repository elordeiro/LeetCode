import copy

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 0 or n == 1:
            return intervals
        
        intervals = sorted(intervals)
        res = []
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if start <= s <= end:
                end = max(end, e)
            else:
                res.append([start, end])
                start = s
                end = e
        
        res.append([start, end])
        return res





if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,4],[2,3]]
    print(sol.merge(intervals))
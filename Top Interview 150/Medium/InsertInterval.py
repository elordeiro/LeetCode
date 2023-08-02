class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        
        res = []
        start, end = newInterval
        
        while intervals:
            s, e = intervals.pop(0)
            if s <= start <= e:
                if s <= end <= e:
                    res.append([s, e])
                    return res + intervals[:]
                res.append([s, e])
                start = s
                break
            elif start < s or end < s:
                intervals.insert(0, [s, e])
                break
            res.append([s, e])

        if res:
            s, e = res.pop()
            if start > e:
                res.append([s, e])

        while intervals:
            s, e = intervals.pop(0)
            if s <= end <= e:
                end = e
                break
            elif end < s:
                intervals.insert(0, [s, e])
                break
        
        res.append([start, end])
        
        while intervals:
            res.append(intervals.pop(0))
        
        return res





if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,2],[3,4],[7,8],[9,10],[12,16]]
    newInterval = [4,7]
    
    intervals = [[1,5]]
    newInterval = [6,8]

    intervals = [[1,5]]
    newInterval = [4,8]
    
    intervals = [[1,5]]
    newInterval = [2,3]
    
    intervals = [[1,5]]
    newInterval = [0,3]
    
    # intervals = [[1,3],[6,9]]
    # newInterval = [2,5]
    print(sol.insert(intervals, newInterval))
        
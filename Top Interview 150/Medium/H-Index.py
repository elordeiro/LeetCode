class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None:
            return 0
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1
        
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if citations[i] <= i:
                return i
    
        return i + 1


if __name__ == "__main__":
    sol = Solution()
    citations = [11,15]
    print(sol.hIndex(citations))
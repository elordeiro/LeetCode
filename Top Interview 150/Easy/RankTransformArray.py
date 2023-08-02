class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dict = {}
        sorted_array = sorted(arr)
        
        rank = 1
        for num in sorted_array:
            if num not in dict:
                dict[num] = rank
                rank += 1
        
        ranks = []
        for num in arr:
            ranks.append(dict[num])
        return ranks

if __name__ == "__main__":
    sol = Solution()
    arr = [27, 46, -3, -36, 31, -14, -7, -36, 27, -14, 41, -40, 23]
    print(sol.arrayRankTransform(arr))

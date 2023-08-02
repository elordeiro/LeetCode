class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for num in arr:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        count = []
        for num in dict:
            curr = dict[num]
            if curr not in count:
                count.append(curr)
            else:
                return False
        
        return True



if __name__ == "__main__":
    sol = Solution()
    # arr = [-3,0,1,-3,1,1,1,-3,10,0]
    arr = [1,2]
    print(sol.uniqueOccurrences(arr))
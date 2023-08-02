import heapq

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_volume = 0 
        
        while i < j:
            max_volume = max(max_volume, (min(height[i], height[j]) * (j - i)))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_volume





if __name__ == "__main__":
    sol = Solution()
    height = [1,2,4,3]
    print(sol.maxArea(height))
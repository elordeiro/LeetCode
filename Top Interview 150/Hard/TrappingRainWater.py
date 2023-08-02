class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        water = 0
        left_max, right_max = 0, 0

        while l <= r:
            left, right = height[l], height[r]
            if left <=right:
                if left >= left_max:
                    left_max = left
                else:
                    water += left_max - left
                l += 1
            else:
                if right >= right_max:
                    right_max = right
                else:
                    water += right_max - right
                r -= 1

        return water


if __name__ == "__main__":
    sol = Solution()
    height = [
                [5,5,1,7,1,1,5,2,7,6],  #23
                [0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2], #26
                [0,1,0,2,1,0,1,3,2,1,2,1], #6 
                [5,4,1,2], #1
                [4,2,3], # 1
                [9,6,8,8,5,6,3], # 3 
                [2,3,4,1,6,6,6,1,0,1], # 4
            ]
    for h in height:
        print(sol.trap(h))

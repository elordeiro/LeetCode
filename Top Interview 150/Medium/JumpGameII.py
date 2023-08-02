import heapq

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        n = len(nums) - 1
        pq = []
        heapq.heappush(pq, (n - nums[0] + 1, nums[0], 0))
        counter = -1
        while pq:
            counter += 1
            heur, value, index = heapq.heappop(pq)
            if index == n:
                break
            if index + value >= n:
                counter += 1
                break
            for i in range(1, value+1):
                try:
                    heapq.heappush(pq, (n - (index+i) - nums[index+i] + counter, nums[index+i], index+i))
                except:
                    break
        return counter

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1]
    print(sol.jump(nums))
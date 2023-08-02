import heapq

class KthLargest(object):
    k = 0
    pq = []
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        for num in nums:
            heapq.heappush(self.pq, num)
        
        return None

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.pq, val)
        
        temp = []
        kth_largest = None
        
        for _ in range(self.k - 1):
            heapq._heapify_max(self.pq)
            temp.append(heapq.heappop(self.pq))
        heapq._heapify_max(self.pq)
        kth_largest = heapq.heappop(self.pq)
        
        heapq.heappush(self.pq, kth_largest)
        while temp:
            heapq.heappush(self.pq, temp.pop())
        
        return kth_largest
        

if __name__ == "__main__":
    k = 1
    nums = []
    obj = KthLargest(k, nums)
    sol = []   
    sol.append(obj.add(-3))
    sol.append(obj.add(-2))
    sol.append(obj.add(-4))
    sol.append(obj.add(0))
    sol.append(obj.add(4))
    print(sol)
    
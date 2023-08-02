class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        nums1[m:] = nums2
        i = m - 1
        j = n - 1
        k = m + n - 1
        

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
if __name__ == "__main__":
    sol = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    sol.merge(nums1, m, nums2, n)
    print(nums1)
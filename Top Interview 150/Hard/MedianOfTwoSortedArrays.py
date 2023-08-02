class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged = sorted(merged)
        length = len(merged)
        if length % 2 == 1:
            return merged[length//2]
        return (merged[length//2] + merged[(length//2) - 1]) / 2.0


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(sol.findMedianSortedArrays(nums1, nums2))
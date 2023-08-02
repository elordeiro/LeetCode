class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


if __name__ == "__main__":
    sol = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(sol.strStr(haystack, needle))

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        i = 0
        j = len(num) - 1
        while i < j:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    x = 121
    print(sol.isPalindrome(x))
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        forwards = []
        backwards = []
        for char in s:
            if char.isalpha() or char.isnumeric():
                forwards.append(char.lower())
                backwards.append(char.lower())
        
        for char in forwards:
            if char == backwards.pop():
                continue
            else:
                return False
        return True



if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = "0P"
    print(sol.isPalindrome(s))
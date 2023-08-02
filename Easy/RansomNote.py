class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, '', 1)
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("aac", "baa"))

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words = reversed(words)

        string = ""
        for word in words:
            string += word + " "
        
        return string.strip()
    

if __name__ == "__main__":
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))
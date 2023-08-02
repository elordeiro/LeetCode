class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        list_of_substrings = []
        
        for char in s:
            if char not in substring:
                substring += char
            else:
                list_of_substrings.append(substring)
                i = substring.find(char)
                substring = substring[i+1:] + char
        list_of_substrings.append(substring)
        
        longest = 0
        for i in range(len(list_of_substrings)):
            length = len(list_of_substrings[i])
            if length > longest:
                longest = length
             
        return longest

if __name__ == "__main__":
        sol = Solution()
        s = "pwwkew"
        print(sol.lengthOfLongestSubstring(s))
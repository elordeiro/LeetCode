class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(words) != len(pattern):
            return False
        
        dict = {}
        word_set = set()
        words = s.split()
        
        for i, char in enumerate(pattern):
            if words[i] not in word_set:
                word_set.add(words[i])
                dict[char] = words[i]
        
        for i, word in enumerate(words):
            try:
                if dict[pattern[i]] != word:
                    return False
            except:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    pattern = "abba"
    s = "dog dog dog dog"
    print(sol.wordPattern(pattern, s))
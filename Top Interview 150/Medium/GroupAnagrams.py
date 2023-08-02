class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}

        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in dict:
                dict[sorted_word] = [word]
            else:
                dict[sorted_word].append(word)
        
        res = []
        for word in dict:
            res.append(dict[word])
        
        return res



if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))
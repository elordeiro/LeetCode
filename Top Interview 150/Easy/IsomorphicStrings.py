class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        _set = set()

        for i, char in enumerate(s):
            if t[i] not in _set:
                dict[char] = t[i]
                _set.add(t[i])
        
        new_string = ""
        for char in s:
            try:
                new_string += dict[char]
            except:
                return False

        return new_string == t
        


if __name__ == "__main__":
    sol = Solution()
    s = "paper"
    t = "title"
    print(sol.isIsomorphic(s, t))
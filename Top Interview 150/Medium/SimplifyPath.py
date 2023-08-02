class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        path = path.split(sep='/')
        for word in path:
            if word:
                if word == '.':
                    continue
                if word == "..":
                    if len(res) > 0:
                        res.pop()
                else:
                    res.append(word)
        
        return '/' + '/'.join(res)

                






if __name__ == "__main__":
    sol = Solution()
    path = "/a/./b/../../c/"
    print(sol.simplifyPath(path))

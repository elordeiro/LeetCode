class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = {}
        start, end, counter, minStart, minLen, size = 0, 0, len(t), 0, float('inf'), len(s)

        for char in t:
            map[char] = map.get(char, 0) + 1

        while end < size:
            if map.get(s[end], 0) > 0:
                counter -= 1
            
            map[s[end]] = map.get(s[end], 0) - 1
            end += 1
            while counter == 0:
                if end - start < minLen:
                    minStart = start
                    minLen = end - start
                
                map[s[start]] += 1
                if map[s[start]] > 0:
                    counter += 1
                start += 1
        
        return s[minStart:minStart+minLen] if minLen != float('inf') else ""





if __name__ == "__main__":
    sol = Solution()
    tests =  [
                ("ADOBECODEBANC", "ABC", "BANC"),
                ("a", "a", "a"),
                ("a", "aa", ""),
                ("ab", "a", "a"),
                ("ab", "b", "b"),
                ("ab", "A", ""),
                ("abc", "cba", "abc"),
                ("abc", "ab", "ab"),
                ("acbbaca", "aba", "baca"),
                ("cabefgecdaecf", "cae", "aec"),
                ("cabwefgewcwaefgcf", "cae", "cwae"),
                ("aaflslflsldkalskaaa", "aaa", "aaa"),
             ]
    
    res = []
    failed = []
    ok = True
    
    for i, test in enumerate(tests, start=1):
        s, t, expected = test
        output = sol.minWindow(s, t)
        res.append((output, expected))
        if output != expected:
            ok = False
            failed.append((i, output, expected))
    if ok:
        print("Passed All Tests")
    else:
        print("Failed Tests:")
        for fail in failed:
            test_num, output, expected = fail
            print(f"Test Number: {test_num}, Output: {output}, Expected: {expected}")
        print()
    print(res)
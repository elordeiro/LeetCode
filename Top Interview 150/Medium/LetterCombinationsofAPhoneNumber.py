class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        keypad = {"2": "abc",
                  "3": "def",
                  "4": "ghi",
                  "5": "jkl",
                  "6": "mno",
                  "7": "pqrs",
                  "8": "tuv",
                  "9": "wxyz"}
        
        n = len(digits)
        sol = []
        
        def loop(i, partial_sol):
            if i >= n:
                sol.append(partial_sol)
                return
            curr = digits[i]
            for letter in keypad[curr]:
                partial_sol += letter
                loop(i+1, partial_sol)
                partial_sol = partial_sol[:-1]
        loop(0, "")

        return sol


if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
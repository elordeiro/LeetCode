class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        string_array = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                string_array.append("FizzBuzz")
            elif i % 5 == 0:
                string_array.append("Buzz")
            elif i % 3 == 0:
                string_array.append("Fizz")
            else:
                string_array.append(str(i))
        
        return string_array

if __name__ == "__main__":
    sol = Solution()
    result = sol.fizzBuzz(15)
    print(result)

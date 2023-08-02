class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        stk = ""
        if x < 0:
            stk += '-'
            x *= -1
        stk += '0'
        while x > 0:
            stk += str(x % 10)
            x //= 10
        
        num = int(stk)
        return num if -2147483648 <= num <= 2147483647 else 0




if __name__ == "__main__":
    sol = Solution()
    x = 1534236469
    print(sol.reverse(x))
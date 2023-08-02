class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []
        while n not in seen:
            seen.append(n)
            
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            n = sum
            
            if sum == 1:
                return True
        
        return False



if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.isHappy(n))
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for digit in digits:
            num += str(digit)
        num = int(num) + 1

        digits = []
        while num > 0:
            digits.insert(0, num % 10)
            num //= 10
        
        return digits

if __name__ == "__main__":
    sol = Solution()
    digits = [1,2,9]
    print(sol.plusOne(digits))
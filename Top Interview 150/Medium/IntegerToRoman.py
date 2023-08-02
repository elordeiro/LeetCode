class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {
                    1:   'I',
                    4:   'IV',
                    5:   'V',
                    9:   'IX',
                    10:  'X',
                    40:  'XL',
                    50:  'L',
                    90:  'XC',
                    100: 'C',
                    400: 'CD',
                    500: 'D',
                    900: 'CM',
                    1000:'M'
               }
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        str = ""
        for x in integers:
            if num >= x:
                temp = num // x
                str += dict[x] * temp
                num -= x * temp

        return str


if __name__ == "__main__":
    sol = Solution()
    num = 58
    print(sol.intToRoman(num))
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry_bit = 0
        sum = ""
        while i >= 0 and j >= 0:
            a_bit = int(a[i])
            b_bit = int(b[j])
            if a_bit and b_bit:
                if carry_bit:
                    sum += "1"
                else:
                    sum += "0"
                carry_bit = 1
            elif a_bit or b_bit:
                if carry_bit:
                    sum += "0"
                else:
                    sum += "1"
            elif carry_bit:
                sum += "1"
                carry_bit = 0
            else:
                sum += "0"
            i -= 1
            j -= 1

        while i >= 0:
            a_bit = int(a[i])
            if a_bit:
                if carry_bit:
                    sum += "0"
                else:
                    sum += "1"
            else:
                if carry_bit:
                    sum += "1"
                    carry_bit = 0
                else:
                    sum += "0"
            i -= 1
        
        while j >= 0:
            b_bit = int(b[j])
            if b_bit:
                if carry_bit:
                    sum += "0"
                else:
                    sum += "1"
            else:
                if carry_bit:
                    sum += "1"
                    carry_bit = 0
                else:
                    sum += "0"
            j -= 1

        if carry_bit:
            sum += "1"
        
        return sum[::-1]
"""
 1
 11
 11
110
"""
if __name__ == "__main__":
    sol = Solution()
    # nums = [1,3,5,7,9]
    # target = 2
    a = "110010"
    b = "10111"
    print(sol.addBinary(a, b))
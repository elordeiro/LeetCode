class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step_count = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -=1
            step_count += 1
        
        return step_count

if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSteps(14))

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers) 
        if target > 0:
            for j in range(n-1,-1,-1):
                if numbers[j] <= target:
                    for i in range(j-1,-1,-1):
                        if numbers[i] + numbers[j] == target:
                            return [i+1,j+1]
        elif target < 0:
            for j in range(n):
                if numbers[j] > target:
                    for i in range(j-1,-1,-1):
                        if numbers[i] + numbers[j] == target:
                            return [i+1,j+1]
        else:
            i = 0
            j = n - 1
            while i <= j:
                temp = numbers[i] + numbers[j]
                if temp == 0:
                    return [i+1,j+1]
                elif temp > 0:
                    j -= 1
                else:
                    i += 1



if __name__ == "__main__":
    sol = Solution()
    numbers = [-10,-8,-2,1,2,5,6]
    target = 0
    print(sol.twoSum(numbers, target))
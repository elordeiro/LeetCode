class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:                      # Edge case: If there is only 1 number in the array, we're already at the end
            return True
        
        j = len(nums) - 1                       # We start from the end of the array
        i = j - 1

        while j >= 0:                           # While there are numbers left to check
            if nums[j] == 0:                    # If we are looking at a 0
                i = j - 1                       # Index i is the number prior to it
                if j + 1 == len(nums):          # If this 0 is at the end of the array
                    while i >= 0:               # Continue looking till the beginning of the array
                        if nums[i] >= j - i:    # If this new number is greater than or equal to the distance to our 0
                            break               # Then we break out of the loop
                        i -= 1                  # If it is not, we continue going down the array
                    else:                       
                        return False            # If we didn't break out of the loop, there is a 0 that we can't jump over
                else:                           # If the 0 is not at the end of the array
                    while i >= 0:               # Continue looking till the beginning of the array
                        if nums[i] > j - i:     # If this new number is greater than the distance to our 0
                            break               # Then we break out of the loop
                        i -= 1                  # If it is not, we continue going down the array
                    else:                       
                        return False            # If we didn't break out of the loop, there is a 0 that we can't jump over
            j -= 1                              # If the number is not a 0 we just ignore it

        return True                             # If we get to the end of the array without any problematic 0's, we return True




if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))
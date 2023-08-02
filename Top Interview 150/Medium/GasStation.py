class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank_reserve = []
        tank_sum = 0
        index = 0
        current_tank = 0
        for i in range(len(gas)):
            temp = gas[i] - cost[i]
            tank_reserve.append(temp)
            tank_sum += temp
            current_tank += temp
            if current_tank < 0:
                current_tank = 0
                index = i + 1
        
        if tank_sum < 0:
            return -1 
        else:
            return index
        

if __name__ == "__main__":
    sol = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    # gas = [2,3,4]
    # cost = [3,4,3]
    # gas =  [1,1,1,1,1,1,1,1,1,1]
    # cost = [1,1,1,1,1,2,1,1,1,1]
    print(sol.canCompleteCircuit(gas, cost))
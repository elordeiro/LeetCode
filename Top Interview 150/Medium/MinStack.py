import heapq

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val <= self.min:
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

        


if __name__ == "__main__":
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]
    test_case = []
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    test_case.append(obj.getMin())
    test_case.append(obj.pop())
    test_case.append(obj.getMin())
    # test_case.append(obj.top())
    print(test_case)
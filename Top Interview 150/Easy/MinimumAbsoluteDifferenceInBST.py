# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getInOrder(self, root, list):
        if root is None:
            return
        self.getInOrder(root.left, list)
        list.append(root.val)
        self.getInOrder(root.right, list)
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        list = []
        self.getInOrder(root, list)
        min = float('inf')

        for i in range(len(list) - 1):
            curr_min = list[i + 1] - list[i]
            if curr_min < min:
                min = curr_min
        return min
        
        
        
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=7)
    root.left = TreeNode(val=3)
    root.right = TreeNode(val=10)
    root.left.left = TreeNode(val=1)
    root.left.right = TreeNode(val=5)
    
    print(sol.getMinimumDifference(root))
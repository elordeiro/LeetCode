# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        targetSum -= root.val
        if targetSum == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)



if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=5)
    root.left = TreeNode(val=4)
    root.left.left = TreeNode(val=12)
    root.left.left.left = TreeNode(val=7)
    root.left.left.right = TreeNode(val=2)
    root.right = TreeNode(val=8)
    root.right.left = TreeNode(val=14)
    root.right.right = TreeNode(val=4)
    root.right.right.right = TreeNode(val=1)
    print(sol.hasPathSum(root, 22))
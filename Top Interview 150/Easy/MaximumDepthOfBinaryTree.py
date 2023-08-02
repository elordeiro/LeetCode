# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=3)
    root.left = TreeNode(val=9)
    root.right = TreeNode(val=20)
    root.right.left = TreeNode(val=15)
    root.right.right = TreeNode(val=7)
    print(sol.maxDepth(root))
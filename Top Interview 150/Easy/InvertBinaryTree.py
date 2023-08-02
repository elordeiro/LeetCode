# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        


def printTree(root):
    if root == None:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=4)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=7)
    root.left.left = TreeNode(val=1)
    root.left.right = TreeNode(val=3)
    root.right.left = TreeNode(val=6)
    root.right.right = TreeNode(val=9)
    
    printTree(root)
    print()
    root = sol.invertTree(root)
    printTree(root)
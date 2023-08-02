# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flattenHelper(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return root
        if not root.left:
            return self.flattenHelper(root.right)
        elif root.left and not root.right:
            root.right = root.left
            root.left = None
            return self.flattenHelper(root.right)
        else:
            right = root.right
            temp = self.flattenHelper(root.left)
            root.right = root.left
            root.left = None
            temp.right = right
            return self.flattenHelper(right)

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.flattenHelper(root)

    def printTree(self, root):
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    sol.printTree(root)
    print()
    sol.flatten(root)
    sol.printTree(root)
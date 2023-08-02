class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def helper(self, root, pathNum):
        pathNum += str(root.val)
        if root.left is None and root.right is None:
            return int(pathNum)
        total = 0
        if root.left:
            total += self.helper(root.left, pathNum)
        if root.right:
            total += self.helper(root.right, pathNum)
        return total

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.helper(root, '')
        return 0


    def printTree(self, root):
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print(sol.sumNumbers(root))
    
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inOrder = []
        self.traverse(root)
        sorted_list = sorted([*set(self.inOrder)])
        return self.inOrder == sorted_list

    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.inOrder.append(root.val)
            self.traverse(root.right)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(0)
    root.left = TreeNode(-1)
    # root.right = TreeNode(7)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(8)
    print(sol.isValidBST(root))
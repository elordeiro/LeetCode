class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.stack = []
        self.traverse(root)

        curr = self.stack.pop()
        k -= 1
        while k > 0:
            self.traverse(curr.right)
            curr = self.stack.pop()
            k -= 1
        return curr.val

    def traverse(self, root):
        while root:
            self.stack.append(root)
            root = root.left


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(sol.kthSmallest(root, 6))
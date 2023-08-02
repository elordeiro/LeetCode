class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dict = {}
        if root:
            self.traverse(root, dict, 0)
        return [*dict.values()]
    
    def traverse(self, root, dict, level):
        if level not in dict:
            dict[level] = root.val
        if root.right:
            self.traverse(root.right, dict, level+1)
        if root.left:
            self.traverse(root.left, dict, level+1)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    # root.right.right = TreeNode(4)
    print(sol.rightSideView(root))
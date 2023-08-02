class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = p = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = q = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    test1 = [3,5,1,6,2,0,8,7,4]
    test2 = [3,5,1,6,2,0,8,7,4]
    # for i in test1:
    #     for j in test2:
    #         print(f"i: {i}, j: {j}, LCA: {sol.lowestCommonAncestor(root, i, j)}")
    print(sol.lowestCommonAncestor(root, p, q).val)
    
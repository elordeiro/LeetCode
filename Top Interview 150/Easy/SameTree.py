# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        if self.isSameTree(p.left, q.left):
            return self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    sol = Solution()
    p = TreeNode(val=1)
    p.left = TreeNode(val=2)
    p.right = TreeNode(val=4)
    
    q = TreeNode(val=1)
    q.left = TreeNode(val=2)
    q.right = TreeNode(val=3)
    
    print(sol.isSameTree(p, q))
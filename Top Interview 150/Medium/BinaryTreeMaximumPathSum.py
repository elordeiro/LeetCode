class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath = float('-inf')
        
        def getMaxPath(root):
            left = max(getMaxPath(root.left), 0) if root.left else 0
            right = max(getMaxPath(root.right), 0) if root.right else 0
            left_root_right = left + root.val + right

            if left_root_right > self.maxPath:
                self.maxPath = left_root_right
            
            return root.val + max(left, right)

        getMaxPath(root)
        return self.maxPath

"""
        1
     /     \
   -2      -3
   / \     /
  1   3  -2
 /
-1
"""
if __name__ == "__main__":
    sol = Solution()
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    
    # root = TreeNode(1)
    # root.left = TreeNode(-2)
    # root.right = TreeNode(-3)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(-2)
    # root.left.left.left = TreeNode(-1)
    
    # root = TreeNode(2)
    # root.left = TreeNode(-1)
    # root.right = TreeNode(-3)
    
    
    print(sol.maxPathSum(root))
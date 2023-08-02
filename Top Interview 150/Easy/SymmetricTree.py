# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preOrder(self, root, list):
        if root == None:
           list.append('Null')
           return
        list.append(root.val)
        self.preOrder(root.left, list)
        self.preOrder(root.right, list)
    
    def postOrder(self, root, list):
        if root == None:
           list.append('Null')
           return
        self.postOrder(root.left, list)
        self.postOrder(root.right, list)
        list.append(root.val)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        preOrder = []
        postOrder = []
        self.preOrder(root, preOrder)
        self.postOrder(root, postOrder)
        
        i = 0
        j = len(preOrder) - 1
        n = j
        while i < n:
            if preOrder[i] != postOrder[j]:
                return False
            i += 1
            j -=1

        return True



if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=2)
    root.left.left = TreeNode(val=3)
    root.left.right = TreeNode(val=4)
    root.right.left = TreeNode(val=4)
    root.right.right = TreeNode(val=3)
    
    print(sol.isSymmetric(root))
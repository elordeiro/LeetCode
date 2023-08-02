# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict = {}
        for i, val in enumerate(inorder):
            dict[val] = i
        
        def helper(postStart, postEnd, inStart, inEnd):
            if postStart > postEnd or inStart > inEnd:
                return None
            root = TreeNode(postorder[postEnd])
            rootIdx = dict[root.val]
            rightNums = inEnd - rootIdx

            root.left = helper(postStart, postEnd-rightNums-1, inStart, rootIdx-1)
            root.right = helper(postEnd-rightNums, postEnd-1, rootIdx+1, inEnd) 
            return root
        
        return helper(0, len(postorder)-1, 0, len(inorder)-1)

    def printTree(self, root):
        if root:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)



if __name__ == "__main__":
    sol = Solution()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    # inorder = [3,2,1]
    # postorder = [3,2,1]
    
    root = sol.buildTree(inorder, postorder)
    sol.printTree(root)


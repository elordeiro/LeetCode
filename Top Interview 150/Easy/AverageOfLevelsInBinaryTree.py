# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traverseTree(self, root, depth, dict):
        if root == None:
            return
        if depth in dict:
            dict[depth].append(root.val)
        else:
            dict[depth] = [root.val]
        self.traverseTree(root.left, depth + 1, dict)
        self.traverseTree(root.right, depth + 1, dict)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        dict = {}
        self.traverseTree(root, 0, dict)

        result = []
        for i in range(len(dict)):
            result.append(sum(dict[i]) / float(len(dict[i])))
        return result




if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(val=3)
    root.left = TreeNode(val=9)
    root.right = TreeNode(val=20)
    root.right.left = TreeNode(val=15)
    root.right.right = TreeNode(val=7)
    
    print(sol.averageOfLevels(root))
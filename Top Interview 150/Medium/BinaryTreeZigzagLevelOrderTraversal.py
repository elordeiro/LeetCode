class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dict = {}
        if root:
            self.traverse(root, dict, 0)
        sol = []
        for i, (k, v) in enumerate(dict.items()):
            if i % 2 == 0:
                sol.append(v)
            else:
                sol.append(v[::-1])

        return sol

    def traverse(self, root, dict, level):
        if level in dict:
            dict[level].append(root.val)
        else:
            dict[level] = [root.val]
        if root.left:
            self.traverse(root.left, dict, level+1)
        if root.right:
            self.traverse(root.right, dict, level+1)



if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sol.zigzagLevelOrder(root))
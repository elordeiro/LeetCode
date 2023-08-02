class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._traverse(root)

    def _traverse(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        next = self.stack.pop()
        self._traverse(next.right)
        return next.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False


def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    printTree(root)
    print()
    sol = []
    obj = BSTIterator(root)
    sol.append(obj.next())
    sol.append(obj.next())
    sol.append(obj.hasNext())
    sol.append(obj.next())
    sol.append(obj.hasNext())
    sol.append(obj.next())
    sol.append(obj.hasNext())
    sol.append(obj.next())
    sol.append(obj.hasNext())
    print(sol)
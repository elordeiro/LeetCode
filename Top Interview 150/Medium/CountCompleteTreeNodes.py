class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height, total = self.get_max_height(root, 0, 0)
        level = 0
        curr = root
        stack = [(curr, level)]
        while curr:
            if curr.right:
                level += 1
                if level == height:
                    break
                stack.append((curr, level))
                curr = curr.right
            elif curr.left:
                total -= 1
                level += 1
                if level == height:
                    break
                stack.append((curr, level))
                curr = curr.left
            else:
                total -= 2
                if level == height:
                    break
                curr, level = stack.pop()
                curr = curr.left
        return total if total > 0 else 1

    def get_max_height(self, root, height, total):
        if root is None:
            return (height-1, total)
        return self.get_max_height(root.left, height+1,total+(2**height))
            
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    print(sol.countNodes(root))
    
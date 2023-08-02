# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def createTree(self, root, num):
        if root is None:
            root = TreeNode(val=num)
            return root
        if num < root.val:
            root.left = self.createTree(root.left, num)
        elif num > root.val:
            root.right = self.createTree(root.right, num)
        return root
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        mid = len(nums) // 2
        head = None
        head = self.createTree(head, nums[mid])
        head.left = self.sortedArrayToBST(nums[0:mid])
        head.right = self.sortedArrayToBST(nums[mid + 1:])
        return head


def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,3,4,5]
    root = sol.sortedArrayToBST(nums)
    printTree(root)
    
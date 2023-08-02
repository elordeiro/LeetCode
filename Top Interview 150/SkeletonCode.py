# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def skeleton(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums[:]):
            if nums[i] % 2 == 0:
                nums.remove(nums[i])

        print(nums)



if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,6,4,5,6,7,8]
    print(sol.skeleton(nums))

    # root = TreeNode(val=4)
    # root.left = TreeNode(val=2)
    # root.right = TreeNode(val=7)
    # root.left.left = TreeNode(val=1)
    # root.left.right = TreeNode(val=3)
    # root.right.left = TreeNode(val=6)
    # root.right.right = TreeNode(val=9)
    
    # head = ListNode(3)
    # head.next = ListNode(2)
    # head.next.next = ListNode(0)
    # head.next.next.next = ListNode(-4)
    # head.next.next.next.next = head.next
    
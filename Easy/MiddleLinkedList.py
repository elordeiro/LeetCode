# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            else:
                break
            slow = slow.next
        return slow

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=3)
    head.next.next.next = ListNode(val=4)
    head.next.next.next.next = ListNode(val=5)
    # head.next.next.next.next.next = ListNode(val=6)

    curr = sol.middleNode(head)
    while curr is not None:
        print(curr.val)
        curr = curr.next

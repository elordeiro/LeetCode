# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        slow = head
        fast = head
        
        for _ in range(n):
            fast = fast.next
            length += 1
        
        if not fast:
            return head.next

        while fast.next:
            length += 1
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head


def printList(head):
    if head is None:
        return
    print(head.val)
    printList(head.next)

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2
    printList(head)
    print()
    head = sol.removeNthFromEnd(head, n)
    printList(head)
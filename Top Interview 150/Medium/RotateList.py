# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        k = k % n
        if k == 0:
            return head
        
        old_head = head
        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        head = slow.next
        slow.next = None
        fast.next = old_head
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
    k = 7
    printList(head)
    print()
    head = sol.rotateRight(head, k)
    printList(head)
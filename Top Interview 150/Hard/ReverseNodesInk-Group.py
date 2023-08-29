class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        if k > length:
            return head
        
        prev = None
        curr = head
        prev_last = None
        new_head = None
        
        i = 0
        while curr:
            if i + k > length:
                break
            for _ in range(k):
                i += 1
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            first, last, head = prev, head, curr
            last.next = curr
            if prev_last:
                prev_last.next = first
            prev_last = last
            if not new_head:
                new_head = first

        return new_head


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    printList(head)
    print()
    k = 2
    head = sol.reverseKGroup(head, k)
    printList(head)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        next = head.next

        while next:
            if curr.val == next.val:
                while curr and curr.val == next.val:
                    curr = curr.next
                if prev is not None:
                    prev.next = curr
                else:
                    head = curr
                try:
                    next = curr.next
                except:
                    break
            else:
                prev = curr
                curr = next
                next = next.next
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
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)
    printList(head)
    print()
    head = sol.deleteDuplicates(head)
    printList(head)
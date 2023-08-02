# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller = ListNode(0)
        greater = ListNode(0)
        first_of_smaller = smaller
        first_of_greater = greater
        
        curr = head
        while curr:
            if curr.val < x:
                smaller.next = curr
                smaller = smaller.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        greater.next = None
        smaller.next = first_of_greater.next
        return first_of_smaller.next
 


def printList(head):
    if head is None:
        return
    print(head.val)
    printList(head.next)

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    x = 3
    printList(head)
    print()
    head = sol.partition(head, x)
    printList(head)
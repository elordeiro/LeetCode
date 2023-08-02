# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head is None or head.next is None or right - left == 0:
            return head
        
        prev = None
        curr = head
        
        n = left - 1
        for _ in range(n):
            prev = curr
            curr = curr.next
        last_before_list = prev
        first_of_list = curr
        
        n = right - left + 1
        for _ in range(n):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        if last_before_list:
            last_before_list.next = prev
        else:
            head = prev
        first_of_list.next = curr
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
    printList(head)
    print()
    left = 2
    right = 4
    head = sol.reverseBetween(head, left, right)
    printList(head)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        sum = ListNode()
        head = sum
        while l1 and l2:
            carry = (l1.val + l2.val + carry)
            sum.next = ListNode(val=carry % 10)
            carry //= 10
            l1 = l1.next
            l2 = l2.next
            sum = sum.next
        
        while l1:
            carry = (l1.val + carry)
            sum.next = ListNode(val=carry % 10)
            carry //= 10
            l1 = l1.next
            sum = sum.next
        while l2:
            carry = (l2.val + carry)
            sum.next = ListNode(val=carry % 10)
            carry //= 10
            l2 = l2.next
            sum = sum.next
        
        if carry == 1:
            sum.next = ListNode(val=1)
            
        return head.next



if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(val=2)
    l1.next = ListNode(val=4)
    l1.next.next = ListNode(val=3)
    l1.next.next.next = ListNode(val=4)
    
    l2 = ListNode(val=5)
    l2.next = ListNode(val=6)
    l2.next.next = ListNode(val=4)

    curr = sol.addTwoNumbers(l1, l2)
    while curr:
        print(curr.val)
        curr = curr.next
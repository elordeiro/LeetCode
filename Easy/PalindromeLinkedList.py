import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        linked_list = []
        
        while curr is not None:
            linked_list.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr is not None:
            if curr.val != linked_list.pop():
                return False
            curr = curr.next

        return True
    
head = ListNode(val=1)
head.next = ListNode(val=2)
head.next.next = ListNode(val=2)
head.next.next.next = ListNode(val=1)

sol = Solution()
print(sol.isPalindrome(head))

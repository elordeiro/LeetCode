import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = ListNode()
        head = curr
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(val=list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(val=list2.val)
                curr = curr.next
                list2 = list2.next
    
        while list1:
            curr.next = ListNode(val=list1.val)
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = ListNode(val=list2.val)
            curr = curr.next
            list2 = list2.next
    
        return head.next

        
if __name__ == "__main__":
    sol = Solution()
    list1 = ListNode(val=1)
    list1.next = ListNode(val=2)
    list1.next.next = ListNode(val=4)
    
    list2 = ListNode(val=1)
    list2.next = ListNode(val=3)
    list2.next.next = ListNode(val=4)

    curr = sol.mergeTwoLists(list1, list2)
    while curr:
        print(curr.val)
        curr = curr.next
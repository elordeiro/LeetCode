import time

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists:
            length = len(lists)
        
            if length > 2:
                half = length >> 1
                return self.mergeKLists([self.mergeKLists(lists[:half]), self.mergeKLists(lists[half:])])

            l1 = lists[0]
            l2 = lists[1] if length > 1 else None
            head = ListNode()
            curr = head
            
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                    curr = curr.next
                else:
                    curr.next = l2
                    l2 = l2.next
                    curr = curr.next
            
            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
            
            return head.next
        


def printList(head):
    if head is None:
        return
    print(head.val)
    printList(head.next)


if __name__ == "__main__":
    sol = Solution()
    
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    l3 = ListNode(-1)
    l3.next = ListNode(6)
    start_time = time.time()
    head = sol.mergeKLists([l1, l2, l3])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Runtime: {round(elapsed_time, 10)}s")
    printList(head)

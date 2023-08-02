# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        unordered_set = set()
        curr = head
        while curr:
            if curr not in unordered_set:
                unordered_set.add(curr)
            else:
                return True
            curr = curr.next
        return False

if __name__ == "__main__":
    sol = Solution()
    [3,2,0,-4]
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(sol.hasCycle(head))
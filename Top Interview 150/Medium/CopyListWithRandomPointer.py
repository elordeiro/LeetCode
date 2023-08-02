import copy

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        
        dict = {}
        curr = head
        
        while curr:
            dict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            try:
                dict[curr].next = dict[curr.next]
            except:
                dict[curr].next = None
            try:
                dict[curr].random = dict[curr.random]
            except:
                dict[curr].random = None
            curr = curr.next
        
        return dict[head]



    def printList(self, head):
        if not head:
            return
        print(head.val)
        self.printList(head.next)



if __name__ == "__main__":
    sol = Solution()
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    sol.printList(node1)
    print()
    new_list = sol.copyRandomList(node1)
    
    node1.next.val = 99
    sol.printList(new_list)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        n = len(arr)
        arr1 = self.sortArr(arr[:(n//2)])
        arr2 = self.sortArr(arr[(n//2):])
        
        temp = self.mergeArrs(arr1, arr2)
        curr = head
        for x in temp:
            curr.val = x
            curr = curr.next
        return head
    
    def sortArr(self, arr):
        if not arr or len(arr) == 1:
            return arr
        
        n = len(arr)
        arr1 = self.sortArr(arr[:(n//2)])
        arr2 = self.sortArr(arr[(n//2):])
        
        return self.mergeArrs(arr1, arr2)
    
    def mergeArrs(self, arr1, arr2):
        arr1_len = len(arr1)
        arr2_len = len(arr2)
        sol = []
        i, j = 0, 0
        while i < arr1_len and j < arr2_len:
            if arr1[i] <= arr2[j]:
                sol.append(arr1[i])
                i += 1
            else:
                sol.append(arr2[j])
                j += 1
        
        while i < arr1_len:
            sol.append(arr1[i])
            i += 1
        while j < arr2_len:
            sol.append(arr2[j])
            j += 1

        return sol



def printList(head):
    if head is None:
        return
    print(head.val)
    printList(head.next)

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    printList(head)
    print()
    head = sol.sortList(head)
    # print(sol.sortList(head))
    printList(head)

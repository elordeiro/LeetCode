final class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class MergeKSortedLists {
    MergeKSortedLists () {}
    
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        return mergeKLists(lists, 0, lists.length - 1);
    }

    private ListNode mergeKLists(ListNode[] lists, int start, int end) {
        if (start == end) return lists[start];
        int mid = (start + end) >> 1;
        ListNode l1 = mergeKLists(lists, start, mid);
        ListNode l2 = mergeKLists(lists, mid + 1, end);
        return mergeTwoLists(l1, l2);
    }
    
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode curr = head;
        
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            }
            else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        
        curr.next = l1 != null ? l1 : l2;
        return head.next;
    }

    public void printList (ListNode head) {
        if (head == null) return;
        System.out.println(head.val);
        printList(head.next);
    }

    public static void main (String[] args) {
        MergeKSortedLists sol = new MergeKSortedLists();
    
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(5);
        
        ListNode l2 = new ListNode(1);
        l2.next = new ListNode(3);
        l2.next.next = new ListNode(4);
        
        ListNode l3 = new ListNode(-1);
        l3.next = new ListNode(6);
        
        ListNode[] arr = {l1, l2, l3};
        long startTime = System.nanoTime();
        ListNode head = sol.mergeKLists(arr);
        long endTime = System.nanoTime();
        long elapsedTime = endTime - startTime;
        System.out.printf("Runtime: %.10fs%n", elapsedTime / 1_000_000_000.0);
        sol.printList(head);
    }
}

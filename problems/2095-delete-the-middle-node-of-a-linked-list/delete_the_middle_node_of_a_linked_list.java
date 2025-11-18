// Problem:  2095. Delete The Middle Node Of A Linked List
// Solution:  double pointers ~ O(n)
// Link:  https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        // initialize the slow pointer to a dummy node before head
        // this ensures we find the node before the middle node
        ListNode dummy = new ListNode(0, head);
        ListNode slow = dummy;
        ListNode fast = head;

        // handle special case single node
        if (head.next == null) return null;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // point the node before to the node after (deleting) the middle node
        slow.next = slow.next.next;

        return head;
    }
}
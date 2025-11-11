// Problem:  2. Add Two Numbers
// Solution:  Recursive approach ~ O(max(n,m))
// Link:  https://leetcode.com/problems/add-two-numbers/


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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumbersRecursive(l1, l2, 0);
    }

    private ListNode addTwoNumbersRecursive(ListNode l1, ListNode l2, int carry) {
        // Base case; both lists have been emptied and no carry left
        if (l1 == null && l2 == null && carry == 0) return null;

        int sum = carry;

        if (l1 != null) {
            sum += l1.val;
            l1 = l1.next;
        }
        if (l2 != null) {
            sum += l2.val;
            l2 = l2.next;
        }

        carry = sum / 10;
        
        return new ListNode(sum % 10, addTwoNumbersRecursive(l1, l2, carry));
    }
}
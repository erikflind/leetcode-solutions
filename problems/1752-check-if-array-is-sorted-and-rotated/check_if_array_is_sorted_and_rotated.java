// Problem:  1752. Check If Array Is Sorted And Rotated
// Solution:  single-pass descent detection ~ O(n)
// Link:  https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution {
    public boolean check(int[] nums) {
        int decreases = 0;
        int n = nums.length;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                decreases++;
            }
        }

        // a valid sorted array can only have one decrease
        return decreases <= 1;
    }
}

// Problem:  9. Palindrome Number
// Solution:  Two pointers ~ O(log X)
// Link:  https://leetcode.com/problems/palindrome-number/

class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);

        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}
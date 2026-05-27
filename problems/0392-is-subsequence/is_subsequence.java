// Problem:  392. Is Subsequence
// Solution:  Two Pointers ~ O(t) [t = String length]
// Link:  https://leetcode.com/problems/is-subsequence/

class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0; // s index
        int j = 0; // t index

        int sLength = s.length();
        int tLength = t.length();

        while (i < sLength && j < tLength) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }
        
        return i == sLength;
    }
}

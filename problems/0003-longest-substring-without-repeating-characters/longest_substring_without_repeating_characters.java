// Problem:  3. Longest Substring Without Repeating Characters
// Solution:  Sliding window + last-seen index map ~ O(n)
// Link:  https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> seen = new HashMap<>();
        int startIndex = 0;
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            Integer previousIndex = seen.get(current);
            
            if (previousIndex != null && previousIndex >= startIndex) {
                startIndex = previousIndex + 1;
            }

            seen.put(current, i);              
            maxLength = Math.max(maxLength, i - startIndex + 1);
        }
        return maxLength;
    }
}

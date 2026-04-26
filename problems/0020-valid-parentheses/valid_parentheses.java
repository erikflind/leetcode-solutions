// Problem:  20. Valid Parentheses
// Solution:  <approach> ~ <complexity> [TODO]
// Link:  https://leetcode.com/problems/valid-parentheses/

class Solution {
    public boolean isValid(String s) {
        Stack<Character> seen = new Stack<>();
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put('}', '{');
        pairs.put(']', '[');

        for (char c : s.toCharArray()) {
            if (!pairs.containsKey(c)) {
                seen.push(c);
            } else if (seen.empty() || seen.pop() != pairs.get(c)) {
                return false;
            }
        }

        return seen.empty();
    }
}

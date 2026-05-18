// Problem:  13. Roman To Integer
// Solution:  HashMap ~ O(n)
// Link:  https://leetcode.com/problems/roman-to-integer/

import java.util.Map;

class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> map = Map.of(
            'I', 1,
            'V', 5,
            'X', 10,
            'L', 50,
            'C', 100,
            'D', 500,
            'M', 1000
        );
        
        int total = 0;
        int previous = -1;

        for (int i = s.length() - 1; i >= 0; i--) {
            int current = map.get(s.charAt(i));

            if (current < previous) {
                total -= current;
            } else {
                total += current;
            }
            previous = current;
        }

        return total;
    }
}

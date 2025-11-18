// Problem:  383. Ransom Note
// Solution:  array ~ O(n + m) -> lengths of the two input strings
// Link:  https://leetcode.com/problems/ransom-note/

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        // "supply" of letters that can be used to build the ransomNote
        HashMap<Character, Integer> supply = new HashMap<Character, Integer>();

        for (int i = 0; i < magazine.length(); i++) {
            char letter = magazine.charAt(i);
            if (!supply.containsKey(letter)) {
                supply.put(letter, 1);
            } else {
                supply.put(letter, supply.get(letter) + 1);
            }
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            char letter = ransomNote.charAt(i);
            if (!supply.containsKey(letter) || supply.get(letter) == 0) {
                return false;
            }
            supply.put(letter, supply.get(letter) - 1);
        }

        return true;
    }
}
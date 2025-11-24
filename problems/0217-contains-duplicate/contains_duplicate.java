// Problem:  217. Contains Duplicate
// Solution:  HashSet ~ O(n)
// Link:  https://leetcode.com/problems/contains-duplicate/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> visited = new HashSet<>();

        for (int num : nums){
            if (visited.contains(num)) {
                return true;
            } else {
                visited.add(num);
            }
            
        }
        
        return false;
    }
}
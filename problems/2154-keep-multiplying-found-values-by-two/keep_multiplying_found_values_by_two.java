// Problem:  2154. Keep Multiplying Found Values By Two
// Solution:  HashSet ~ O(n)
// Link:  https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution {
        public int findFinalValue(int[] nums, int original) {
            /* While the brute force solution (looping over the array each step)
             * has a worst-case time of O(n^2), we can achieve better results
             * by taking a hash-based approach (HashSet).
             * 
             * In the first loop we add each element to the set, resulting in
             * a time complexity of O(n).
             * 
             * In the second loop, we check to see if the current value of
             * "original" is in the set - this check is O(1). In the worst case, 
             * we run at most n + 1 loop iterations, giving us O(n).
             * 
             * Overall, this gives us a time complexity of: O(n) + O(n) = O(n).
             *
             * Since we add all the elements to a new data structure, the
             * space complexity is O(n).
            */            
            HashSet<Integer> set = new HashSet<>(nums.length);

            for (int num : nums) {
                set.add(num);
            }
            
            while (set.contains(original)) {
                original *= 2;
            }

        return original;
    }
}
// Problem:  1. Two Sum
// Solution:  iterative, HashMap ~ O(n)
// Link:  https://leetcode.com/problems/two-sum/


import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> visited = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int number = nums[i];
            int difference = target - number;

            if (visited.containsKey(difference)) {
                return new int[]{i, visited.get(difference)};
            }

            visited.put(number, i);
        }
        throw new IllegalArgumentException();
    }
}
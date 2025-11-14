// Problem:  1672. Richest Customer Wealth
// Solution:  iterative ~ O(m*n) 
// Link:  https://leetcode.com/problems/richest-customer-wealth/

class Solution {
    public int maximumWealth(int[][] accounts) {
        int highestWealth = -1;
        
        for (int i = 0; i < accounts.length; i++) {
            int sum = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                sum += accounts[i][j];
            }
            if (sum > highestWealth) highestWealth = sum;
        }
        return highestWealth;
    }
}
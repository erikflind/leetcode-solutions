// Problem:  122. Best Time To Buy And Sell Stock Ii
// Solution:  Single-pass greedy ~ O(n)
// Link:  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution {
    public int maxProfit(int[] prices) {
        int maxTotal = 0;
        int difference;

        for (int i = 1; i < prices.length; i++) {
            difference = prices[i] - prices[i - 1];

            if (difference > 0) {
                maxTotal += difference;
            }
        }

        return maxTotal;
    }
}

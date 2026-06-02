// Problem:  121. Best Time To Buy And Sell Stock
// Solution:  Single pass minimum price tracking ~ O(n)
// Link:  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    public int maxProfit(int[] prices) {        
        int minPrice = prices[0];
        int currentPrice;
        int profit;
        int maxProfit = 0;

        for (int i = 1; i < prices.length; i++) {
            currentPrice = prices[i];
            profit = currentPrice - minPrice;

            if (profit > maxProfit) {
                maxProfit = profit;
            }

            if (currentPrice < minPrice) {
                minPrice = currentPrice;
            }
        }

        return maxProfit;
    }
}

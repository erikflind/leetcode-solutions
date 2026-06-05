// Problem:  3683. Earliest Time To Finish One Task
// Solution:  single pass ~ O(n)
// Link:  https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution {
    public int earliestTime(int[][] tasks) {
        int earliestFinish = Integer.MAX_VALUE;

        for (int[] task : tasks) {
            earliestFinish = Math.min(earliestFinish, task[0] + task[1]);
        }

        return earliestFinish;
    }
}

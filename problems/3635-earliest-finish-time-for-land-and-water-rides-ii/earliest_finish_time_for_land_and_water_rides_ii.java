// Problem:  3635. Earliest Finish Time For Land And Water Rides II
// Solution:  Greedy scan multiple passes ~ O(n + m)  [n == landStartTime.length, m == waterStartTime.length]
// Link:  https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int earliestLandFinish = Integer.MAX_VALUE;
        int earliestWaterFinish = Integer.MAX_VALUE;

        int earliestLandFirst = Integer.MAX_VALUE;
        int earliestWaterFirst = Integer.MAX_VALUE;

        for (int i = 0; i < landStartTime.length; i++) {
            earliestLandFinish = Math.min(earliestLandFinish, landStartTime[i] + landDuration[i]);
        }

        for (int i = 0; i < waterStartTime.length; i++) {
            earliestWaterFinish = Math.min(earliestWaterFinish, waterStartTime[i] + waterDuration[i]);
            earliestLandFirst = Math.min(earliestLandFirst, Math.max(earliestLandFinish, waterStartTime[i]) + waterDuration[i]);
        }

        for (int i = 0; i < landStartTime.length; i++) {
            earliestWaterFirst = Math.min(earliestWaterFirst, Math.max(earliestWaterFinish, landStartTime[i]) + landDuration[i]);
        }

        return Math.min(earliestLandFirst, earliestWaterFirst);
    }
}

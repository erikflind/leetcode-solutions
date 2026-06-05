// Problem:  3633. Earliest Finish Time For Land And Water Rides I
// Solution:  Brute force ~ O(n * m)  [n == landStartTime.length, m == waterStartTime.length]
// Link:  https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
// Note:  brute force is the *intended* approach for this version of the problem, 
//        a more efficient solution can be found in the follow-up question (problem #3635)

class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {        
        int earliestFinish = Integer.MAX_VALUE;
        
        for (int i = 0; i < landStartTime.length; i++) {
            int landFinish = landStartTime[i] + landDuration[i];

            for (int j = 0; j < waterStartTime.length; j++) {
                int waterFinish = waterStartTime[j] + waterDuration[j];

                int finishLandThenWater = Math.max(landFinish, waterStartTime[j]) + waterDuration[j];
                int finishWaterThenLand = Math.max(waterFinish, landStartTime[i]) + landDuration[i];

                earliestFinish = Math.min(earliestFinish, Math.min(finishLandThenWater, finishWaterThenLand));
            }
        }

        return earliestFinish;
    }
}

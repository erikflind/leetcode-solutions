// Problem:  3190. Find Minimum Operations To Make All Elements Divisible By Three
// Solution:  loop ~ O(n)
// Link:  https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

int minimumOperations(int* nums, int numsSize) {
    int counter = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 3 > 0) counter++;
    }
    return counter;
}
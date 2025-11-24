// Problem:  1018. Binary Prefix Divisible By 5
// Solution:  loop ~ O(n)
// Link:  https://leetcode.com/problems/binary-prefix-divisible-by-5/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    bool *answer = malloc(numsSize);

    int remainder = 0;

    for (int i = 0; i < numsSize; i++) {
        remainder = (2 * remainder + nums[i]) % 5;  // could left-shift instead of multiply
        answer[i] = remainder == 0;
    }

    return answer;
}
// Problem:  1342. Number Of Steps To Reduce A Number To Zero
// Solution:  iterative ~ O(log n)
// Link:  https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

int numberOfSteps(int num) {
    int counter = 0;

    while (num > 0) {
        if (num % 2 == 0) {
            num /= 2;
        } else {
            num -= 1;
        }
        counter++;
    }
    return counter;
}

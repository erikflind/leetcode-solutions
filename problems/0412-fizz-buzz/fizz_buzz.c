// Problem:  412. Fizz Buzz
// Solution:  iterative ~ O(n)
// Link:  https://leetcode.com/problems/fizz-buzz/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// imports
#include <stdlib.h>
#include <string.h>

// macros
#define FIZZ 3
#define BUZZ 5

// helper methods
char * intToString(int n) {
    // Note: assumes positive integer since context is FizzBuzz,
    // otherwise we'd check for sign.

    // Constraints also states that n != 0, 
    // so we don't need to handle this special case.

    int length = 0;
    int copy = n;
    int i = 0;

    // find length of string representation
    while (copy > 0) {
        copy /= 10;
        length++;
    }

    char *ptr = malloc(length + 1);

    // copy over digits to string
    for (i; i < length; i++) {
        ptr[i] = '0' + n % 10;
        n /= 10;
    }
    
    // add null terminator
    ptr[i] = '\0';

    // reverse string to get correct order (using XOR method)
    for (int j = 0, k = i - 1; j < k; j++, k--) {
        ptr[j] = ptr[j] ^ ptr[k];
        ptr[k] = ptr[j] ^ ptr[k];
        ptr[j] = ptr[j] ^ ptr[k];
    }

    return ptr;
}


// main logic
char ** fizzBuzz(int n, int *returnSize) {
    // We assume malloc always works to make the code cleaner,
    // good practice would be to always check for NULL return value.

    char **result = malloc(sizeof(char *) * n);
    *returnSize = n;

    for (int i = 1; i <= n; i++) {
        int index = i - 1;  // array of strings index

        if (i % FIZZ == 0 && i % BUZZ == 0) {
            const char *word = "FizzBuzz";
            result[index] = malloc((strlen(word) + 1)); 
            strcpy(result[index], word);
            
        } else if (i % FIZZ == 0) {
            const char *word = "Fizz";
            result[index] = malloc((strlen(word) + 1));
            strcpy(result[index], word);

        } else if (i % BUZZ == 0) {
            const char *word = "Buzz";
            result[index] = malloc((strlen(word) + 1));
            strcpy(result[index], word);

        } else {
            result[index] = intToString(i);
        }
    }

    return result;
}

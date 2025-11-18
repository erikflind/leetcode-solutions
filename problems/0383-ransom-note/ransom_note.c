// Problem:  383. Ransom Note
// Solution:  array ~ O(n + m) -> lengths of the two input strings
// Link:  https://leetcode.com/problems/ransom-note/

bool canConstruct(char *ransomNote, char *magazine) {
    char c;
    int i;
    int alphabet[26] = {0};  // initialize array of all 0 values

    for (i = 0; (c = magazine[i]) != '\0'; i++) {
        alphabet[c - 'a']++;
    }

    for (i = 0; (c = ransomNote[i]) != '\0'; i++) {
        if (alphabet[c - 'a'] == 0) return 0;
        alphabet[c - 'a']--;
    }

    return 1;
}
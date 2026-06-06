// Problem:  12. Integer To Roman
// Solution:  Digit-place lookup tables ~ O(1)
// Link:  https://leetcode.com/problems/integer-to-roman/

class Solution {
    public String intToRoman(int num) {
        final String[] M = {"", "M", "MM", "MMM"};
        final String[] C = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        final String[] X = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        final String[] I = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

        StringBuilder sb = new StringBuilder();

        sb.append(M[num / 1000]);
        sb.append(C[num % 1000 / 100]);
        sb.append(X[num % 100 / 10]);
        sb.append(I[num % 10]);

        return sb.toString();
    }
}

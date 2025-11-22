# Problem: 2154. Keep Multiplying Found Values By Two

**Link:** [https://leetcode.com/problems/keep-multiplying-found-values-by-two/](https://leetcode.com/problems/keep-multiplying-found-values-by-two/)

**Summary:**  Input is an array of integers `nums` and an integer `original`. If the current value of `original` can be found in `nums`, multiply `original` by two, else stop. Repeat this using the new value, for as long as the number can be found. Return the **final value** of `original`.

**Solution Approach:**
- HashSet ~ O(n) ~ Java
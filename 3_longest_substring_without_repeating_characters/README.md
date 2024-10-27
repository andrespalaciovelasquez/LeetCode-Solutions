# Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.

### Example 1:

<div style="border-left: 2px solid #555; padding-left: 10px;">

**Input:** s = "abcabcbb" <br>
**Output:** 3<br>
**Explanation:** The answer is "abc", with the length of 3.

</div>

### Example 2:

<div style="border-left: 2px solid #555; padding-left: 10px;">

**Input:** s = "bbbbb" <br>
**Output:** 1 <br>
**Explanation:** The answer is "b", with the length of 1.

</div>

### Example 3:

<div style="border-left: 2px solid #555; padding-left: 10px;">

**Input:** s = "pwwkew" <br>
**Output:** 3 <br>
 **Explanation:** The answer is "wke", with the length of 3. <br>
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

</div>

### Constraints:

- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols and spaces.
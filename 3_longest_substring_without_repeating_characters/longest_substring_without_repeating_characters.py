# Time complexity: O(n) - Linear time complexity
def length_of_longest_substring(s: str) -> int:
    char_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_map and char_map[s[end]] >= start:
            start = char_map[s[end]] + 1

        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length


# Example 1:
s1 = "abcabcbb"
print(length_of_longest_substring(s1))  # Output: 3

# Example 2:
s2 = "bbbbb"
print(length_of_longest_substring(s2))  # Output: 1

# Example 3:
s3 = "pwwkew"
print(length_of_longest_substring(s3))  # Output: 3

def longest_palindrome(s: str) -> str:
    reverse_s = s[::-1]
    palindrome = ""
    left = 0
    right = left + 1

    while right <= len(s):
        substring = reverse_s[left:right]

        if substring in s:
            if substring == substring[::-1] and len(substring) > len(palindrome):
                palindrome = substring
            right += 1
        else:
            left += 1
            right = left + 1

    return palindrome


# Example 1:
input_string = "babad"
result = longest_palindrome(input_string)
print(result)  # "aba"

# Example 2:
input_string = "cbbd"
result = longest_palindrome(input_string)
print(result)  # Output: "bb"

# Example 3:
input_string = "abacdfgdcaba"
result = longest_palindrome(input_string)
print(result)  # Output: aba

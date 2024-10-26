s = "abacdfgdcaba"
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

print(palindrome)  # Output: aba
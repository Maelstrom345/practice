def is_palindrome(s):
    s = "".join(char.lower() for char in s if char.isalnum())

    return s == s[::-1]

print(is_palindrome("rarar"))
print(is_palindrome("level"))
print(is_palindrome("note"))
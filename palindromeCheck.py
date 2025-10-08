# Task: Check if a string reads the same forward and backward
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


print(is_palindrome("Race car"))  # True

# Converts to lowercase and removes spaces before comparing with its reverse.

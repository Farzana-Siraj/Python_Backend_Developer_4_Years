"""A palindrome is a string or number that reads the same forward and backward.
"madam"      → True
"racecar"   → True
"python"    → False
121          → True
"""
# BEST & MOST PYTHONIC (Slicing Allowed)
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("malayalam"))
# ----------------------------------

# BEST INTERVIEW ANSWER (Without slicing)
# use two pointers from both ends and compare characters.
def is_palindromes(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindromes("madam"))
# ------------------------------

# Palindrome Check for Numbers (Reverse logic)
def is_palindrome_num(n):
    original = n
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return rev == original

print(is_palindrome_num(121))
# ------------------------------

# Case-Insensitive & Ignore Spaces/Punctuation (Real-World)
import re

def is_palindrom(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrom("A man, a plan, a canal: Panama"))
# ------------------------------

"""
Complexity
| Method       | Time     | Space    |
| ------------ | -------- | -------- |
| Slicing      | O(n)     | O(n)     |
| Two-pointer  | **O(n)** | **O(1)** |
| Number logic | O(n)     | O(1)     |

Edge Cases Interviewers Ask
| Input     | Output               |
| --------- | -------------------- |
| `""`      | True                 |
| `"a"`     | True                 |
| `"Aa"`    | Depends on case rule |
| `"12321"` | True                 |

"""
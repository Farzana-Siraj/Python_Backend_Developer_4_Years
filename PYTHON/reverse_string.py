s = "python"

# with slicing (best practice)
reversed_s = s[::-1]
print(reversed_s)
# -------------------------------------

# without slicing

# (best practice) --> list + loop + join() --> Time Complexity: O(n) Space Complexity: O(n)
def reverse_string(s):
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)

print(reverse_string("python"))

# ---------------------------------------
rev = ""
# --------

#  using loop --> Time Complexity: O(n²) (string concatenation) -- beginner level
# Since Python strings are immutable, repeated concatenation is inefficient.
for ch in s:
    rev = ch + rev

# Using a loop (efficient way) --> Time Complexity: O(n²)
for i in range(len(s)-1, -1, -1):
    rev += s[i]

# Using while loop (classic logic test) --> Time Complexity: O(n²)
i = len(s) - 1

while i >= 0:
    rev += s[i]
    i -= 1

# Using recursion --> Time Complexity: O(n) Space Complexity: O(n)
def reverse_recursive(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_recursive(s[:-1])
        # return reverse_string(s[1:]) + s[0]

# Using stack concept (DS approach)
stack = list(s)

while stack:
    rev += stack.pop()

# --------
print(rev)
# ----------------------------------------------
# Word-wise reverse (different problem),  O(n) time
s = "Hello World from Python"

# --------with slicing-------
print(" ".join(s.split()[::-1]))
# output: Python from World Hello

# ----------without slicing--------
def reverse_words(s):
    words = s.split()
    rev_words = []
    for i in range(len(words) - 1, -1, -1):
        rev_words.append(words[i])
    return " ".join(rev_words)
print(reverse_words(s))
# --------OR--------
print("".join(reversed(s)))  # using built-in reversed() function


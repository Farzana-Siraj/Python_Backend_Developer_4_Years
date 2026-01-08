"""
Check if Two Strings Are Anagrams (Interview-Ready Guide)
Two strings are anagrams if they contain the same characters with the same frequency,
but possibly in a different order.
Example:
listen  ↔  silent  → True
evil    ↔  vile    → True
hello   ↔  world   → False
"""
# BEST & MOST PYTHONIC (Recommended) - Time complexity: O(n log n) (due to sorting)
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
# ----------------------------------------

# BEST INTERVIEW ANSWER (O(n) time – NO sorting)
# use a frequency dictionary to get linear time complexity.
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True
# ----------------------------------------

# Using collections.Counter (Clean & Professional) o(n)
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
# ----------------------------------------

# Case-Insensitive Anagram Check
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
# ----------------------------------------

# Ignore Spaces & Punctuation (Real-World Case)
import re
from collections import Counter

def is_anagram(s1, s2):
    s1 = re.sub(r'\W+', '', s1.lower())
    s2 = re.sub(r'\W+', '', s2.lower())
    return Counter(s1) == Counter(s2)

print(is_anagram("Dormitory", "Dirty room"))

# ----------------------------------------
print(is_anagram("listen", "silent"))
# ----------------------------------------
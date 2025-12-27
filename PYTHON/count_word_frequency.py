# BEST & MOST PYTHONIC WAY --> Using collections.Counter
# Counter is optimized and ideal for frequency counting
from collections import Counter

text = "python is easy and python is powerful"
words = text.split()

freq = Counter(words)
print(freq)
# ----------------------------------------

# WITHOUT using Counter (Very common interview constraint) O(n) time
def word_frequency(text):
    freq = {}
    for word in text.split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
# ---------OR(if built-in functions allowed)---------
# from collections import defaultdict

# def word_frequency(text):
#     freq = defaultdict(int)
#     for word in text.split():
#         freq[word] += 1
#     return dict(freq)
# -----------------------------------------

text = "python is easy and python is powerful"
print(word_frequency(text))
# -------------------------------------------

# Case-Insensitive Word Count
def word_frequency_case_insensitive(text):
    freq = {}
    for word in text.lower().split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
# -------------------------------------------

# Handle Punctuation (Real-world data)
import re

text = "Python, is easy! And python is powerful."
words = re.findall(r'\b\w+\b', text.lower()) #extracts all words from a sentence, ignoring punctuation,

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
# -------------------------------------------

# Using defaultdict
from collections import defaultdict

text = "python is easy and python is powerful"
#If a key is accessed for the first time, it will automatically get value 0. Because int() → 0
# This avoids manual checks like 'if word in freq'
freq = defaultdict(int) 

for word in text.split():
    freq[word] += 1

# Converts defaultdict to a normal dict
print(dict(freq))
# -------------------------------------------

# Most Common Interview Follow-Ups
def top_n_frequent_words(text, n):
    freq = word_frequency(text)
    sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]

# Top 3 most frequent words
Counter(words).most_common(3)

# Word frequency from a file
with open("file.txt") as f:
    words = f.read().lower().split()

# Frequency sorted by count
sorted(freq.items(), key=lambda x: x[1], reverse=True)

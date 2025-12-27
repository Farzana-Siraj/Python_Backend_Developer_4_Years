d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# ----------------------------------------
# BEST & MOST PYTHONIC (Python 3.9+)
merged = d1 | d2
# merged = d1 | d2 | d3 # For merging more than 2 dictionaries
# ----------------------------------------

# Most Common Interview Answer (All Python versions) 3.5+
merged = {**d1, **d2}
# merged = {**d1, **d2, **d3} # For merging more than 2 dictionaries
# ----------------------------------------

# Using update() (In-place merge) - Modifies d1 - Good when mutation is allowed
d1.update(d2)
print(d1)

# for multiple dictionaries
d3 = {'d': 5}
merged = {}
for d in (d1, d2, d3):
    merged.update(d)

print(merged)
# ----------------------------------------

# Manual Merge (No shortcuts – logic round)
merged = {}
for k, v in d1.items():
    merged[k] = v
for k, v in d2.items():
    merged[k] = v

# multiple dictionaries
for d in (d1, d2, d3):
    for k, v in d.items():
        merged[k] = v
# ----------------------------------------

# Merge and SUM values for common keys (Tricky interview follow-up)
# can use same for multiple dictionaries also
from collections import defaultdict
merged = defaultdict(int)

for d in (d1, d2):
    for k, v in d.items():
        merged[k] += v

print(dict(merged))

# ----------------------------------------
print(merged)
# ----------------------------------------
nums = [1, 2, 2, 3, 4, 3, 5]
# ----------------------------------------

# BEST & MOST PYTHONIC (Order NOT important)
# short, fast, o(n), order is not preserved
unique = list(set(nums))
# ----------------------------------------

# BEST INTERVIEW ANSWER (Order PRESERVED) set + loop
def remove_duplicates(nums):
    seen = set() # To track seen elements. Sets automatically store unique values
    result = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

print(remove_duplicates(nums))
# ----------------------------------------

# Using dict.fromkeys() (Pythonic & Order-Preserving) python 3.7+
unique = list(dict.fromkeys(nums))
# ----------------------------------------

# Remove duplicates WITHOUT using set - (Logic-only round) o(n^2)
def remove_duplicates_no_set(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result

print(remove_duplicates_no_set(nums))
# ----------------------------------------

# Using List Comprehension (Not efficient)
unique = []
[unique.append(x) for x in nums if x not in unique]

# ----------------------------------------
print(unique)
# ----------------------------------------
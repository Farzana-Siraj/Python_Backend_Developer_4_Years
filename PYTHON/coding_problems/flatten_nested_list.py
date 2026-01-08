"""Flattens a nested list of integers.
Example:
Input: [1, [2, [3, 4], 5], 6
Output: [1, 2, 3, 4, 5, 6]"""
# BEST & MOST ACCEPTED (Recursive – Handles Any Depth), Time: O(n)
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list): #Checks whether item is a list - only lists need further flattening
            result.extend(flatten(item)) #extend() adds all elements of the returned list to result
        else:
            result.append(item)
    return result
# ----------------------------------------

# Using Stack (NO recursion – Interview favorite)
def flatten_stack(nested_list):
    result = []
    stack = nested_list[::-1]  # Reverse to maintain order
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])  # Reverse to maintain order
        else:
            result.append(item)
    return result
# ----------------------------------------
print(flatten([1, [2, [3, 4], 5], 6]))
# ----------------------------------------

# Using List Comprehension (Only 1-level nesting) - Does NOT work for deep nesting
lst = [1, [2, 3], [4, 5]]
flat = [x for sub in lst for x in sub]
print(flat)
# ----------------------------------------
# Using itertools (Limited)
from itertools import chain

lst = [[1, 2], [3, 4]]
print(list(chain.from_iterable(lst)))
# ----------------------------------------

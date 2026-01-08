# BEST & MOST RECOMMENDED (Single Pass – No Sorting)
# without duplicates
def second_largest_number(arr):
    if len(arr) < 2:
        return None  # Not enough elements for second largest

    largest = second = float('-inf') # Initialize to negative infinity

    for number in arr:
        if number > largest:
            second = largest
            largest = number
        elif largest > number > second: #ignore duplicates
            second = number

    return second if second != float('-inf') else None

print(second_largest_number([10, 5, 20, 8]))
# -------------------------------------------

# Using set() + max() (Clean & Simple)
def second_largest_number_set(arr):
    unique_numbers = set(arr)
    if len(unique_numbers) < 2:
        return None  # Not enough unique elements for second largest
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)
# -------------------------------------------

# Using sorting (NOT recommended for interviews)- less efficient - O(n log n)
def second_largest_number_sort(arr):
    unique_numbers = list(set(arr))
    if len(unique_numbers) < 2:
        return None  # Not enough unique elements for second largest
    unique_numbers.sort()
    return unique_numbers[-2]
#-------------------------------------------

nums = [2, 6, 3, 8, 5]
s = sorted(nums)
print(s[-2])
# -------------------------------------------
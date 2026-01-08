a = 10
b = 20

# ---------------------------------------
# BEST & MOST PYTHONIC WAY --> O(1) time, O(1) space
a, b = b, a
# ---------------------------------------
# using Temp variable
temp = a
a = b
b = temp
# ---------------------------------------
# using arithmetic operations (not recommended for large numbers)
a = a + b
b = a - b
a = a - b
# ---------------------------------------
# using bitwise XOR (only for integers)
a = a ^ b
b = a ^ b
a = a ^ b
# ---------------------------------------
# using multiplication and division (not recommended for zero values)
a = a * b
b = a // b
a = a // b
# ---------------------------------------
print(a, b)

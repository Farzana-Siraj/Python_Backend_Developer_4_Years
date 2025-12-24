# print numbers from n to 0 (-n)
def neg(n):
    for i in range(n, 1):
        print(i, end=" ")


# print numbers from n-1 to 0 (+n)
def pos(n):
    for i in range(n - 1, -1, -1):
        print(i, end=" ")


# squares of natural numbers (1², 2², 3², …) that are ≤ x
def printIncreasingPower(x):
    i = 1
    while i * i <= x:
        print(i * i, end=" ")
        i += 1


# print N's multiplication table
def multiplicationTable(N):
    for i in range(1, 11):
        print(N * i, end=" ")


# print the numbers from x to 0 in decreasing order in a single line.
def printInDecreasing(x):
    while (x >= 0):
        print(x, end=" ")
        x -= 1


# given a string s, print its characters at even indices
def stringJumper(s):
    for i in range(0,len(s),2):
        print(s[i], end="")


# strip()- Remove leading and trailing spaces
def trim(str):
    return str.strip()

# Return starting index , Use: find()
def exists(str, x):
    return str.find(x)

# Convert string to title case : Use: title()
def titleIt(str):
    return str.title()

# Swap uppercase ↔ lowercase
def casesSwap(str):
    return str.swapcase()
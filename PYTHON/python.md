- (a >= 0) **!=** (b >= 0) is True only when one is positive and the other is negative. (**!= is XOR operation**)
- By default, print() adds a newline (\n). To print without a newline, use the **end** parameter.
-- *print(i, end=" ")* - it gives a single space
-- *print(i, end="")* - it doesn't gives a space. printing character and separating characters by nothing.

#### Key Characteristics of range()

- **Memory Efficiency:** range() does not store all values in memory but generates them on demand, making it ideal for large sequences.
- **Immutability:** A range object cannot be changed after creation.

- **Parity** = whether an index is EVEN or ODD

#### String Functions

- **strip()** - Remove leading and trailing spaces
- **find()** - Return starting index
- **title()** - converting string to title case
- **swapcase()** - Swap uppercase ↔ lowercase
- **lower()** - covert to lowercase
- **upper()** - convert to uppercase
- **startswith** - checks begining
- **endswith** - checks ending

**arr.index(x)** - to find the index of element x in array arr

#### slicing

string = "python"
a. string[0:2] = py (Slicing till index 1)
b. string[0:] = python (Slicing till last index)
c. string[0:4] = pyth (Slicing till index 3)
d. string[0:-2] = pyth (Slicing till index -3).
Note: -1 indexing starts from last of any string.
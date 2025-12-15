(a >= 0) **!=** (b >= 0) is True only when one is positive and the other is negative. (**!= is XOR operation**)
By default, print() adds a newline (\n). To print without a newline, use the **end** parameter.                                                  *print(i, end=" ")* - it gives a single space
*print(i, end="")* - it doesn't gives a space. printing character and separating characters by nothing.
#### Key Characteristics of range()
**Memory Efficiency:** range() does not store all values in memory but generates them on demand, making it ideal for large sequences.
**Immutability:** A range object cannot be changed after creation
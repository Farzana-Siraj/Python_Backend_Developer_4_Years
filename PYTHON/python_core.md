# Python Core
## Data Types
| Feature    | List      | Tuple      | Set           | Dict         |
| ---------- | --------- | ---------- | ------------- | ------------ |
| Ordered    | ✅ Yes     | ✅ Yes      | ❌ No          | ✅ Yes (3.7+) |
| Mutable    | ✅ Yes     | ❌ No       | ✅ Yes         | ✅ Yes        |
| Duplicates | ✅ Allowed | ✅ Allowed  | ❌ Not allowed | ❌ Keys only  |
| Indexing   | ✅ Yes     | ✅ Yes      | ❌ No          | ❌ (keys)     |
| Use case   | Sequence  | Fixed data | Uniqueness    | Mapping      |
|    | []     | ()       | {}        | {key: value}      |

### List
- used when order matters and You need to add/remove/update items frequently

### Tuple
- use when Data should not change (e.g., coordinates, configuration), Used as dictionary keys, Slightly faster & safer than lists

### set
- unique elements
- use when You need uniqueness, Fast membership testing (O(1)), Removing duplicates from a list

### Dictionary (dict)
- Ordered (Python 3.7+)
- Keys must be unique & immutable
- Values can be anything
- Very fast lookups (O(1))
- use when Data is mapped (JSON, configs, DB records), Need fast access using keys
---

## Mutable vs Immutable
| Feature          | Mutable         | Immutable       |
| ---------------- | --------------- | --------------- |
| Can change value after creation | ✅ Yes           | ❌ No            |
| content     |      modified | Any “change” creates a new object in memory |
| Memory location  | Same            | New object      |
| Examples| list, dict, set, bytearray | int, str, tuple, float, bool, frozenset |
| Thread safe      | ❌ Less          | ✅ More          |
| Dict key allowed | ❌ No            | ✅ Yes           |
|       | Efficient for frequent updates, Used for collections & state| Safe to use as dict keys, Better for caching & hashing, Avoid side effects|

#### why strings are unmutable?
```bash
s = "hello"
s = s + " world"
```
- Creates a new string, old one stays unchanged
- Helps with memory optimization & thread safety
    - **How Immutability Helps with Memory Optimization**
        1. Object Reuse (**String Interning**)
            - Because immutable objects never change, Python can safely reuse the same object.
            ```bash
            a = "python"
            b = "python"

            print(id(a) == id(b))  # True
            ```
            - Python stores only one "python" object in memory, Both variables point to the same object
            - Huge memory savings when many identical strings exist (logs, JSON keys, configs)
            - ❌ If strings were mutable → changing one would affect all references → unsafe
        2. **Safe Hashing**(Used in dict / set)
            - Immutable objects can be hashed once and reused
            ```bash
            d = {"name": "Farzana"}
            ```
            - "name" hash is computed once.
            - Can be reused forever because value never changes
            - Makes dict lookups fast & memory-efficient
            - ❌ Mutable objects → hash may change → dictionary breaks

    - How Immutability Helps with Thread Safety
        - Problem with Mutable Objects
        ```bash
        shared_list = [1, 2, 3]
        ```
        - If two threads modify it: Race conditions, Data corruption, Need locks (threading.Lock) → slower
        - Immutable Objects = No Race Condition
        ```bash
        shared_str = "hello"
        ```
        - Threads can: Read safely, Never modify it, No locks needed
        - No thread can change the object
        - Every “change” creates a new object
        - Original stays untouched

#### Why Python Uses Immutable Objects Internally
| Area           | Benefit           |
| -------------- | ----------------- |
| Dict keys      | Fast hashing      |
| Sets           | Stable membership |
| Multithreading | No locks          |
| Memory         | Object reuse      |
| Caching        | Safe reuse        |

Immutability allows Python to reuse objects safely, cache their hash values, and avoid synchronization issues in multi-threaded environments, resulting in better memory efficiency and thread safety.
---
| Expression | Type  | Reason              |
| ---------- | ----- | ------------------- |
| `()`       | tuple | Empty tuple         |
| `(1)`      | int   | Just grouping (Parentheses are treated as grouping, not tuple creation)|
| `(1,)`     | tuple | Comma creates tuple |

In Python, tuples are defined by commas, not parentheses
---

#### mutable object inside tuple can change
```bash
t = (1, [2, 3])
t[1].append(4)
print(t)  # (1, [2, 3, 4])
```
---
### is vs ==

#### == → Value Equality
- checks if two objects have the same value
```bash
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True
```
- Values are equal, Objects are different

#### is → Identity Comparison

- checks if both variables refer to the same object in memory.
- (None, True, False, singleton objects)
```bash
print(a is b)   # False
```
- Different memory locations

#### Small Integers (Caching)
```bash
x = 100
y = 100

print(x is y)   # True
```
- Python caches small integers (-5 to 256), but
```bash
x = 1000
y = 1000

print(x is y)   # False (often)
```
---
#### Strings (Interning)
```bash
s1 = "python"
s2 = "python"

print(s1 is s2)   # True
```
- Python reuses it. because, "python" is: Short, Identifier-like (letters only), Very common
- Python automatically interns such strings. So internally: 
```bash
memory
 ┌───────────┐
 │ "python"  │
 └───────────┘
     ▲   ▲
    s1   s2
```
same memory, same object, is → True
But:
```bash
s1 = "py thon"
s2 = "py thon"

print(s1 is s2)   # False
```
Why Python does NOT reuse it:
- Contains a space
- Not identifier-like
- Less predictable
- Python does not automatically intern it

So Python creates two separate string objects:
```bash
memory
 ┌────────────┐     ┌────────────┐
 │ "py thon"  │     │ "py thon"  │
 └────────────┘     └────────────┘
     ▲                  ▲
    s1                 s2
```
- same value, different objects, == → True, is → False

- Python uses an optimization technique called **string interning**.
- Interning = storing only one copy of certain strings and reusing it
- This is possible only because strings are immutable.

- Python interns some immutable strings for memory optimization. Identifier-like strings may share the same object, while others don’t, so is may return True or False depending on interning.
- is checks object identity, and string interning is an optimization, not a language guarantee.

##### can do force interning
```bash
import sys

s1 = sys.intern("py thon")
s2 = sys.intern("py thon")

print(s1 is s2)   # True
```
Now Python is told explicitly: “Store only one copy.”

##### Never use is to compare strings or numbers
Because:
Interning is an implementation detail
Behavior may change
Code becomes unreliable
...
#### Mutable Objects
```bash
a = []
b = []

print(a == b)   # True
print(a is b)   # False
```

#### Correct Use of is
Always use *is* for *None*
```bash
if x is None:
    print("No value")

if x == None:   # Bad practice
```
---
### Truthy and falsy values
In Python, every object is evaluated as either True or False when used in a boolean context such as:
```bash
if value:
    ...
```
- Truthy → behaves like True
- Falsy → behaves like False

#### Falsy Values in Python (IMPORTANT)
Python has only a few falsy values. Complete list of falsy values
```bash
False
None
0
0.0
0j
''
""
[]
()
{}
set()
range(0)
```
example:
```bash
if []:
    print("True")
else:
    print("False")

output:- False
```
##### why empty values are falsy
Python internally checks: Length = 0 → falsy, Length > 0 → truthy
```bash
if len([]) == 0:
    print("Falsy")
```
Same logic for: list, tuple, dict, set, string

```bash
bool("False") # True :- Non-empty string → truthy
bool([False]) # True :- List is not empty
bool(None)   # False
bool(False)  # False
None == False   # False
None is False   # False
```

#### Truthy Values

Everything that is NOT falsy is truthy
examples:- 
```bash
True
1
-1
0.1
" "
"python"
[0]
(0,)
{"a": 1}
set([0])
```
```bash
example:
if " ":
    print("True")
# Space is a character → truthy
```
**How Python Decides (Advanced)**
Python evaluates truth value using:
- __bool__() method
- If not present → __len__()
- If length is 0 → False, else True

Custom class example:
```bash
class Test:
    def __len__(self):
        return 0

print(bool(Test()))  # False
```
In Python, falsy values are False, None, zero values, and empty collections; everything else is truthy.
```bash
if not my_list: # good practice
    print("Empty list")

if my_list == []: # avoid this

```
---
### None
- *None* is a special singleton object in Python that represents “no value” or “absence of a value.”
- It is not 0, not False, and not an empty string.
- None is a singleton. There is only one None object in Python.
```bash
a = None
b = None

print(a is b)   # True
print(type(None)) # <class 'NoneType'>
bool(None)   # False  (None is Falsy)
None == False   # False
None == 0       # False
None == ""      # False
```
- Same memory object, That’s why we use *is* with *None*

#### Why does Python need None?
1. Default return value of functions
2. Placeholder / initialization
3. Optional parameters
4. Representing “no result” safely
```bash
def func():
    pass

print(func())   # None (If no return → Python returns None)
result = None   # value not calculated yet. Used when: Value will be assigned later, Data is missing or unknown
# optimal parameters
def connect(timeout=None):
    if timeout is None:
        timeout = 30
# Representing “no result” safely
user = db.get_user(id)

if user is None:
    print("User not found")
```


---
- (a >= 0) **!=** (b >= 0) is True only when one is positive and the other is negative. (**!= is XOR operation**)
- By default, print() adds a newline (\n). To print without a newline, use the **end** parameter.
    - *print(i, end=" ")* - it gives a single space
    - *print(i, end="")* - it doesn't gives a space. printing character and separating characters by nothing.

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
1. string[0:2] = py (Slicing till index 1)
2. string[0:] = python (Slicing till last index)
3. string[0:4] = pyth (Slicing till index 3)
4. string[0:-2] = pyth (Slicing till index -3).
Note: -1 indexing starts from last of any string.

#### defaultdict

It is a special type of dictionary. It automatically assigns a default value if a key does not exist

### shallow vs deep copy
Shallow copy duplicates only the top-level object and shares nested references, while deep copy duplicates all nested objects, creating a completely independent copy.

#### copying
Copying means creating a new object from an existing one.
#### Shallow Copy
- Creates a new outer object
- Inner (nested) objects are shared
- Changes to nested objects affect both copies
- use when No nested mutable objects, Performance matters

#### Deep Copy
- Creates a new object at all levels
- No shared references
- Fully independent copy
- use when Nested mutable objects exist, You need complete isolation
```bash
a = [1, 2, [3, 4]]

# shallow copy
import copy

b = copy.copy(a)
# OR
b = a.copy()
# OR
b = a[:]

b[0] = 100
b[2].append(5)

print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [100, 2, [3, 4, 5]]
# ----------------------------------

# deepcopy
import copy

b = copy.deepcopy(a)
b[2].append(5)

print(a)  # [1, 2, [3, 4]]
print(b)  # [1, 2, [3, 4, 5]]

```
| Feature           | Shallow Copy | Deep Copy |
| ----------------- | ------------ | --------- |
| Outer object      | New          | New       |
| Inner objects     | Shared       | New       |
| Affects original? | Yes (nested) | No        |
| Memory usage      | Less         | More      |
| Speed             | Faster       | Slower    |
```bash
#  it is assignment, not a copy, No copy created, Both variables point to same object
b = a

# Tuple itself is immutable, Inner list still shared
t = (1, [2, 3])
copy.copy(t)

# dict shallow copy
a = {"x": [1, 2]}
b = a.copy()

b["x"].append(3)
print(a)  # {'x': [1, 2, 3]}

# Real Backend Example
def process(data):
    local = data.copy()   # shallow
    local["status"] = "processed"
# Use deep copy if data contains nested lists/dicts that must not change.

```

### remove, Pop, Del
| Feature             | remove()   | pop()      | del           |
| ------------------- | ---------- | ---------- | ------------- |
| Deletes by          | Value      | Index      | Index / Slice |
| Returns value       | ❌ No       | ✅ Yes      | ❌ No          |
| Deletes multiple    | ❌ No       | ❌ No       | ✅ Yes         |
| Can delete variable | ❌          | ❌          | ✅             |
| Error type          | ValueError | IndexError | IndexError    |

**When to Use What?**
✅ Use **remove()** when:

You know the value
You don’t need the removed item
- remove() deletes by value
- Removes first occurrence of a value
- Searches by value, not index
- Removes only first match
```bash
list.remove(value)

nums = [10, 20, 30, 20]
nums.remove(20)
print(nums)
# [10, 30, 20]

# ❌ Error if value not found
ValueError: list.remove(x): x not in list

```

✅ Use **pop()** when:

You know the index
You need the removed value
- pop() deletes by index and returns the element
- Removes and returns an element
- Uses index (default: last element)
- Returns removed value
- ❌ Error if index out of range
```bash
list.pop(index)

nums = [10, 20, 30]
x = nums.pop()
print(x)     # 30
print(nums)  # [10, 20]

nums.pop(0)
# removes 10

IndexError: pop index out of range
```

✅ Use **del** when:

You want to remove multiple items
You want to delete the object itself
- del deletes by index, slice, or deletes the object itself(variable)
- Does not return anything
- Keyword, not a method
- can delete:- single item, multiple items(slice), entire object.
```bash
# syntax
del list[index]
del list[start:end]
del variable

nums = [10, 20, 30, 40]
del nums[1]
# [10, 30, 40]

del nums[1:3]
# [10]

del nums
# deletes variable completely

```
- Any variable assigned inside a function is treated as local unless declared *global* or *nonlocal*.

#### map()

##### how it works in python 3?

``` bash
map(function, iterable1, iterable2, ...)
```
- The first argument MUST be a callable function
- **map()** applies that function to items from the iterables
``` bash
list(map(None, [1,2], [3,4]))
```
output: Raises TypeError: 'NoneType' object is not callable
**WHY**:- here passed **None** as the function:
        In Python 3:
            None is not callable
            Python tries to do something like:
``` bash
None(1, 3)
```
That is invalid. So Python raises:
```bash
TypeError: 'NoneType' object is not callable
```
but bellow case will work
```bash
list(zip([1,2], [3,4]))

output:- [(1, 3), (2, 4)]
```

##### how it works in python 2?

**output:-** [(1,3), (2,4)]
```bash
map(None, [1,2], [3,4])
```
would zip the iterables

----------------------------------------

```bash
from module import *
```
- controls which names are imported into the current namespace from a module.
- import public names defined in __all__, if available

### How Python decides what to import

Python follows this order:
1. If __all__ is defined in the module
```bash
__all__ = ['a', 'b', 'c']

then:
from module import *

Only the names listed in __all__ are imported
```

2. If __all__ is NOT defined
- it imports all public names.
- All names not starting with underscore _

#### non-local keyword

**role:-** allows modification of variables in an enclosing (non-global) scope.
(nonlocal allows a nested function to modify a variable from its enclosing (but non-global) scope.)
used inside a nested function to refer to a variable that:
- Is not local to the inner function
- Is not global
- Exists in the nearest enclosing (outer) function
- allows reassignment in nested function

##### Why nonlocal is needed?
**Example:-** without nonlocal
```bash
def outer():
    x = 10
    def inner():
        x = 20   # creates a NEW local variable
    inner()
    print(x)

outer()

output: 10
```
**Example:-** with *nonlocal*
```bash
def outer():
    x = 10
    def inner():
        # tells Python: “Use x from the enclosing function, not a new local one.”
        nonlocal x
        x = 20
    inner()
    print(x)

outer()

output: 10
```


-------------------------------------------------
**global keyword:-** role:- refers to variables from the global scope
-------------------------------------

#### pass
- *pass* is a no-operation statement
- It tells Python: “Do nothing here, but keep the syntax valid”
```bash
def f():
    pass

print(f())

output: None
```

#### Function return behavior in Python
In Python:- 
- Every Python function returns a value.
- If a function does not explicitly return a value, it automatically returns None.
This applies to:
- Functions with pass
- Functions without a return statement
- Functions that end without hitting a return

---
```bash
bool([]) --> False ([] is an empty list, Empty collections are False)
bool({}) --> False ({} is an empty dictionary, Empty collections are False)
bool(0) --> False
```
- bool(x) evaluates the truthiness of an object.
- Empty or zero values are considered False
- Non-empty or non-zero values are considered True
- Falsy Values:- 0, 0.00, None, False, ""(empty string), [], {}, (), st()
---
- Mutable default arguments are evaluated once and reused, causing shared state across calls.
-Returning from finally is strongly discouraged because:
- - It suppresses exceptions
- - It hides return values
- - It makes debugging harder
---
#### purpose of __slots__ in class
__slots__ is a class-level attribute used to optimize memory usage and control which attributes instances are allowed to have. it restricts attribute creation and reduces memory usage by avoiding per-instance __dict__.

#### @staticmethod
The @staticmethod decorator defines a method that:
- Does NOT receive self
- Does NOT receive cls
- Behaves like a regular function
- Is namespaced inside the class for logical grouping
- it defines a method that does not depend on the class or instance state.

#### @classmethod

- The @classmethod decorator defines a method that:
    - Receives the class itself as the first argument (cls)
    - Is bound to the class, not to any particular instance
    - Can be called using either the class or an instance
- Binds method to the class, not the instance
- **@classmethod** binds a method to the class and receives the class as its first argument (cls).

#### functools.partial
- is used to fix (pre-fill) some arguments of a function, creating a new function with fewer parameters.
---
- A Python set is an unordered, iterable collection of unique, hashable elements.
---
- **+=** modifies mutable objects in place, while **+** creates a new object.
---
#### Singleton
- In Python, the most Pythonic and robust way to enforce that only one instance of a class is created is by using a metaclass.
(Metaclasses are the most Pythonic and correct way to implement a true Singleton pattern.)
##### Why metaclasses work best for Singleton
- Metaclasses control class creation and instantiation
- They allow you to intercept object creation via __call__
- This ensures exactly one instance, even with inheritance

#### Python’s MRO (Method Resolution Order)
It determines the order in which base classes are searched when looking for a method or attribute.
Python uses an algorithm called **C3 linearization** to compute this order.
- Python 3 uses C3 linearization to compute MRO for multiple inheritance.
- Python 2 used a DFS-like approach
##### What is C3 linearization?
C3 linearization ensures three key properties:
1. Local precedence order
 - A class is searched before its parents
2. Monotonicity
 - Subclasses preserve the ordering of base classes
3. No duplication
 - Each class appears only once in the MRO
This makes multiple inheritance:
- Predictable
- Consistent
- Safe from ambiguity

#### hashable
In Python, an object is hashable if:
- It has a hash value that does not change during its lifetime
- It can be used as a key in a dictionary or an element in a set
👉 Immutability is the key requirement for hashability.
- Mutable objects are not hashable.
- Lists are mutable → not hashable.
- examples:- 
    - hash(frozenset([1, 2, 3]))
    - hash("hello")
    - hash([1, 2, 3])  # TypeError . it is not hashable
    - hash((1, 2, 3))       # valid
    - hash((1, [2], 3))    # TypeError

---
#### How Python’s class hierarchy works?
In Python:
- object is the base class of all classes
- Every built-in and user-defined class inherits from object
So the inheritance chain looks like:
```bash
object
   ↑
  int

issubclass(subclass, superclass)
```
It returns:
- True if the first argument is a subclass of the second
- Otherwise False
All classes in Python inherit from object.

#### generator
A generator expression uses parentheses and produces a generator object lazily.
**example:-**
```bash
(x for x in range(3))
```
A generator expression in Python is defined using:
- Parentheses ()
- An expression followed by a for clause
- It produces values lazily, one at a time
Generators can be iterated only once. After they are exhausted, they produce no values.
#### CPython Interning Caveat
- Python may intern some strings for optimization
- But strings created at runtime (like via join) are NOT guaranteed to be interned
- Therefore, you should never rely on is for string comparison
#### enumerate()
```bash
enumerate(iterable, start=0)
```
**enumerate()** returns an **iterator** that yields (index, value) pairs lazily.
- built-in Python function

#### descriptor protocol method
In Python, a descriptor is an object that defines any of these methods:
```bash
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
```
If a class defines one or more of these, it becomes a descriptor.

##### __get__

This is a core descriptor protocol method
Used to control attribute access
Commonly used in:
- @property
- Django ORM fields
- Custom attribute access logic
---
##### __getattribute__
- Called for every attribute access
- Defined on normal classes

##### __getattr__
- Called only if attribute is not found
- Used for fallback behavior

##### __getitem__
- Used for indexing (obj[key])
- Part of container protocol
---
#### eval()
- eval() evaluates a string as a Python expression and returns its result.
- It executes the expression at runtime
- Returns the result of the expression
- eval() is dangerous when used with untrusted input.
```bash
eval("2+2")  ➜  4
The result is an integer, not a string.

eval() is dangerous when used with untrusted input.
eval("__import__('os').system('rm -rf /')")

Safer alternatives:
ast.literal_eval() (for literals only)
Avoid dynamic evaluation where possible
```
---
#### with statement

- The with statement in Python is used with **context managers** to ensure that setup and cleanup code is handled safely and predictably.
- The with statement guarantees that __exit__() is executed, even if an exception occurs inside the block.
- with does not retry operations, It only manages entry and exit behavior
- with is about resource management

#### lambda

- In Python, lambda expressions have strict syntax rules.
- Lambdas can only contain expressions — not statements like yield, return, try, or for.
- Lambdas are functions → type is function
##### Example:- 
```bash
lambda x: (yield x)

output:- SyntaxError: invalid syntax
```
yield is a statement, not an expression (in this context). Python does not allow yield inside a lambda.
```bash
lambda x=5: x * 2 -> Default arguments are allowed in lambdas
lambda *args: sum(args). --> Variable-length arguments are allowed. Expression-only body (sum(args))
```
---
#### type
- it is a class
- it is a **metaclass** used to create most classes
- it is an instance of itself(type)
- type creates classes
- type inherits from object
```bash
type(type)
output:- type
```
---
#### class
- All classes inherit from object

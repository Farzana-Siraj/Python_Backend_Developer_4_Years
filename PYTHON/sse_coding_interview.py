"""
output: Raises UnboundLocalError
You assign to a (a = 5)
Because of this assignment, Python treats a as a local variable throughout the entire 
function body
"""
a = 10
def f():
    print(a) # ❌ trying to use local 'a' before assignment
    a = 5
f()

# Corrected version
a = 10
def f():
    global a
    print(a)
    a = 5

#-----------------------------------------

def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
print(f())

"""
output:
[1]
[1, 1]
[1, 1, 1]
Why?
The same list object is reused across all calls
This causes unexpected shared state
"""
# Corrected version
def f(x=None):
    if x is None:
        x = []
    x.append(1)
    return x
# This ensures a new list is created per call.
#-----------------------------------------

def test():
    try:
        return "try"
    finally:
        return "finally"

print(test())
"""
output: "finally"
A return statement in a finally block always overrides any previous return from try or except.
"""
#-----------------------------------------
class A:
    pass

a = A()
a.x = 10
a.y = 20
"""
Each object has a __dict__
New attributes can be added dynamically
Uses more memory
"""
# using __slots__ to save memory
class B:
    __slots__ = ['x', 'y']

b = B()
b.x = 10
b.y = 20
b.z = 30  # ❌ AttributeError: 'B' object has no attribute 'z'
"""
Effects:
Prevents creation of attributes not listed in __slots__
Removes per-instance __dict__
Saves memory, especially when creating many objects
"""
#----------static method---------
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

MathUtils.add(2, 3)   # 5
"""No instance required
No access to class or instance data"""

#----------class method---------
class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
Person.get_count()     # valid
p = Person()
p.get_count()          # also valid
"""cls refers to Person
The method operates on class-level data"""

#------------------------------------------

# functools.partial example
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)

print(square(5))
"""output: 25
exp=2 is pre-applied
square() now needs only one argument"""
# ------------------------------------------
x = [1, 2]
y = x
x += [3] #+= on a list calls list.__iadd__(), modifies the list in place, original list object is updated
# x + [3] creates a new list, so output would be [1, 2]
print(y)
# output: [1, 2, 3]
#-------------------------------------------
# Typical metaclass-based Singleton (conceptual)
class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
"""This guarantees:
Only one instance is ever created
Repeated calls return the same object"""
#-------------------------------------------

# Python's MRO uses C3 linearization
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
"""output: [D, B, C, A, object]
This order is calculated using C3 linearization, not simple DFS."""
# ----------------------------------------------
x = "abc" # x refers to a string literal. String literals are often interned by Python (an optimization)
# x is iterable ("a", "b", "c")
y = "".join(x) # creates a new string object. Even though the value is "abc", it is constructed at runtime
print(x is y) # False → compares identity
print(x == y)  # True → compares values
"""
join() creates a new string object, so is returns False even if values are equal.
Always use == for value comparison."""
#---------------enumerate()--------------------
items = ['a', 'b', 'c']

e = enumerate(items)

print(list(e))
"""output:- [(0, 'a'), (1, 'b'), (2, 'c')]
Each yielded element is a tuple
But the return value itself is not a list
"""
#-----------------------

x = (i**2 for i in range(3))
print(sum(x))
print(sum(x))
"""output:- 5
0
This is a generator expression. Generators are iterators. They produce values once, lazily
"""
#-------------------------------
eval("2+2") # 4
eval("'4'") # '4'

#------with statement-----------
obj = expression
obj.__enter__()
try:
    # with-block code
finally:
    obj.__exit__()
# No matter what happens inside the block (even if an exception occurs), __exit__() is always called.

with open("file.txt") as f:
    data = f.read()
    1 / 0   # exception
"""
Even though a ZeroDivisionError occurs, The file is properly closed, Because __exit__() is executed"""
#-------------------------------

a = [1,2,3,4]
b = a
a = a + [4] # creates a new list. [1,2,3,4] + [4] → [1,2,3,4,4]. a is reassigned to this new list
print(b) # b still points to the old list
# output: [1, 2, 3, 4]

#--------------------------------
print(type(lambda: None) is type((lambda: None).__call__))
"""output: False
lambda: None creates a function object. In Python, lambdas are just functions
type(lambda: None) is <class 'function'>
type((lambda: None).__call__) is <class 'method-wrapper'> # (or built-in method type). it is a bound method
Every function object has a __call__ method
A function and its bound __call__ method are different types
Calling a function and calling __call__ are the same thing. They behave similarly, but their types are different."""

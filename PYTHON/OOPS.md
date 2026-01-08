**OOPS** is a programming approach where we design programs using objects and classes instead of only functions and logic.

# Class
A class is a blueprint/template for creating objects.
```bash
class Person:
    pass
```

## Object
An object is an instance of a class.
```bash
p1 = Person()
```

## __init__ Constructor
Used to initialize (assign values to) object properties.
```bash
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ali", 25)
print(p1.name)  # Ali

```

## self
- Refers to the current object
- Mandatory as the first parameter in instance methods
```bash
def greet(self):
    print("Hello", self.name)
```

## Methods
Functions defined inside a class.
```bash
class Person:
    def greet(self):
        print("Hello")

```
### Static Method
```bash
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

### class Method
```bash
class Person:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

```

## Attributes (Variables)
### Instance Variables

Specific to each object.
```bash
self.name = name
```
### Class Variables
Shared by all objects.
```bash
class Person:
    country = "India"
```
## Access Modifiers
| Type      | Syntax  | Meaning              |
| --------- | ------- | -------------------- |
| Public    | `var`   | Accessible anywhere  |
| Protected | `_var`  | Within class & child |
| Private   | `__var` | Only inside class    |

## __str__ and __repr__
```bash
class Person:
    def __str__(self):
        return "Person object"
```

# Abstraction
Hiding implementation details.
```bash
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 4 * 4
```

# Encapsulation
Binding data + methods together
```bash
class Bank:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance # Accessed via method
```
# Inheritance
One class inherits another class.
```bash
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
```
## Types:

### Single

### Multiple

### Multilevel

### Hierarchical

# Polymorphism
Same method name, different behavior
```bash
class Bird:
    def fly(self):
        print("Bird flies")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
```

# Real Time Examples
Django Models → OOPS
- Model = Class
- Row = Object
- Fields = Attributes
- Methods = Business logic


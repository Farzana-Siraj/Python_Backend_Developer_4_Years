## Generator

A **generator** in Python is created when a function uses the yield keyword.
Any function containing yield is a generator function.
Calling it returns a generator object, not a value.
##### Example
```bash
def f():
    yield 42
```
- The presence of yield turns the function into a generator function
- Calling f() returns a generator object
- Values are produced lazily using next()

- (x for x in range(10)) is a generator expression
- ❌ list(x for x in range(10)) - wrapping it with list() consumes the generator Final result is a list, not a generator
- ❌ lambda: yield 42. (yield cannot be used inside lambda)
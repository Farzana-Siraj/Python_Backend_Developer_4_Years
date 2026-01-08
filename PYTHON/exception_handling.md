Exception handling is used to handle runtime errors so that the program doesn’t crash unexpectedly.

# Why Exception Handling?

- Prevent program crash
- Handle invalid user input
- Handle file / DB / network errors
- Improve application reliability

# Common Exceptions in Python
| Exception           | When it occurs         |
| ------------------- | ---------------------- |
| `ZeroDivisionError` | Division by zero       |
| `ValueError`        | Invalid value          |
| `TypeError`         | Wrong data type        |
| `IndexError`        | Invalid index          |
| `KeyError`          | Missing dictionary key |
| `FileNotFoundError` | File not found         |
| `ImportError`       | Module import fails    |

# Try-Except Block
```python
try:
    # Code that might raise an exception
    pass
except ExceptionType:
    # Handle specific exception
    pass
except:
    # Handle any other exception
    pass
finally:
    # Always execute this block (optional)
    pass

# example - Handles specific exceptions
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as e: # Generic Exception
    print("An error occurred:", e)

```
# Generic Exception (Not Recommended Alone)
Use only for logging or last fallback
```python
try:
    a = 10 / 0
except Exception as e:
    print(e)
```

# else Block
Runs only if no exception occurs
```python
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
```

# finally Block
- Always executes, used for cleanup
- Used for DB connections, file close, locks
```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing resources")
    f.close()
```

# Raising Exceptions
Use `raise` to throw exceptions manually. Used for custom validations
```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")
```

# Custom Exceptions
Define your own exception classes by inheriting from `Exception`
```python
class InvalidAgeError(Exception):
    pass

age = 15
if age < 18:
    raise InvalidAgeError("Age must be 18+")
```

# assert Statement
Used for debugging, raises `AssertionError` if condition is false. Disabled in production using -O flag
```python
x = 10
assert x > 0, "x must be positive"
assert x < 5, "x must be less than 5"  # Raises AssertionError
```

# Multiple Exceptions in One Block
```python
try:
    x = int("abc")
except (ValueError, TypeError):
    print("Invalid data")
```

# Best Practices
- Catch specific exceptions
- Avoid bare(empty) except
- Use finally for cleanup
- Log exceptions (logging) for debugging
- Use custom exceptions for clarity
- Validate inputs before processing
- Don’t hide errors


# Real Django Example
```python
from django.http import HttpResponse

def divide(request):
    try:
        x = int(request.GET.get("x"))
        y = int(request.GET.get("y"))
        return HttpResponse(x / y)
    except ZeroDivisionError:
        return HttpResponse("Cannot divide by zero")
    except Exception as e:
        return HttpResponse(str(e))
```
def decorator(func):
    def wrapper(a, b):
        print("before adding")
        result = func(a, b)
        return result
    return wrapper

@decorator
def func(a, b):
    return a + b

print(func(2,3))
print("completed")
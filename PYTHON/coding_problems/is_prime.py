"""
Check if a number is prime.
A natural number greater than 1 that has exactly two distinct positive divisors:
1 and itself.
"""
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        """
        After eliminating even numbers, 
        I check divisibility only by odd numbers up to √n,
        because any composite number must have a factor ≤ √n.
        """
        if n % i == 0:
            return False
    return True
 
num = int(input("enter the number: "))
print(f"{num} is prime: {is_prime(num)}")

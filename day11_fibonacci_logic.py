# Day 11: Loop + Function Combination
# Task: Fibonacci, even/odd count, average

# Fibonacci
def fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

n = int(input("Enter n for Fibonacci: "))
print("Fibonacci series:", fibonacci(n))

# Count even numbers in list
def count_even(numbers):
    return sum(1 for x in numbers if x % 2 == 0)

numbers = list(map(int, input("Enter numbers: ").split()))
print("Total even numbers:", count_even(numbers))

# Average of numbers
def average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average(numbers))

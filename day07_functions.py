# Day 7: Functions
# Task: Add two numbers, factorial, maximum in list

# Function to add two numbers
def add(a, b):
    return a + b

print("Adding 53 and 64:", add(53, 64))

# Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter number for factorial: "))
print("Factorial:", factorial(num))

# Maximum in a list
def maximum(numbers):
    return max(numbers)

numbers_list = list(map(int, input("Enter numbers: ").split()))
print("Maximum number:", maximum(numbers_list))

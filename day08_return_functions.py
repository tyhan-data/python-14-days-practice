# Day 8: Functions with Return
# Task: Square, cube, even numbers from 1 to n

# Square of a number
def square(num):
    return num ** 2

num = int(input("Enter number to square: "))
print("Square:", square(num))

# Cube of a number
def cube(num):
    return num ** 3

num = int(input("Enter number to cube: "))
print("Cube:", cube(num))

# Even numbers from 1 to n
def even_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 == 0]

num = int(input("Enter n to get even numbers: "))
print("Even numbers:", even_numbers(num))

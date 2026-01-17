# Day 1: Variables & Data Types
# Task: Print name and age, arithmetic operations, check number > 10

# Print your name and age
name = 'Tyhan'
age = 20
print(f"Hello! My name is {name} and I am {age} years old.")

# Add, subtract, multiply, divide
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

print("Sum:", num_1 + num_2)
print("Subtraction:", num_1 - num_2)
print("Multiplication:", num_1 * num_2)
print("Division:", num_1 / num_2)

# Check if a number is greater than 10
num = int(input("Enter a number: "))
result = "Yes" if num > 10 else "No"
print("Is the number greater than 10?:", result)

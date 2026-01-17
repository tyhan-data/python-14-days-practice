# Day 10: List Problems
# Task: Sum, remove duplicates, sort descending

# Sum of elements
def summation(numbers):
    return sum(numbers)

numbers = list(map(int, input("Enter numbers: ").split()))
print("Sum:", summation(numbers))

# Remove duplicates
def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))

print("After removing duplicates:", remove_duplicates(numbers))

# Sort descending
def sort_desc(numbers):
    return sorted(numbers, reverse=True)

print("Sorted descending:", sort_desc(numbers))

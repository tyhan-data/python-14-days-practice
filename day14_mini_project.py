# Day 14: Mini Project (Final Practice)
# Task: From a list of numbers, find all even numbers, their sum, and the maximum even number

def operations(numbers):
    """
    Function to find:
    - all even numbers from the list
    - sum of even numbers
    - maximum even number
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    total = sum(even_numbers)
    maximum = max(even_numbers) if even_numbers else None  # safe if no even numbers

    return even_numbers, total, maximum


# Taking input from user
list_numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Performing operations
even_nums, even_sum, max_even = operations(list_numbers)

# Printing results
print("\nResults:")
print("Even numbers:", even_nums)
print("Sum of even numbers:", even_sum)
if max_even is not None:
    print("Maximum even number:", max_even)
else:
    print("No even numbers in the list!")

# Day 3: Lists & Methods
# Task: Add, remove, length, loop through elements

numbers = [10, 20, 30, 40]
print("Original list:", numbers)

# Add 50
numbers.append(50)
# Remove 20
numbers.remove(20)
print("After adding 50 and removing 20:", numbers)

# Length of list
print("Length:", len(numbers))

# Loop through list
print("All elements:")
for num in numbers:
    print(num)

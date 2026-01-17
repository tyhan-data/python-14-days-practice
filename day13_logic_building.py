# Day 13: Logic Building
# Task: Prime check, multiplication table, second largest

# Prime check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number to check prime: "))
print("Is prime?:", "Yes" if is_prime(num) else "No")

# Multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i*n}")

num = int(input("Enter number for multiplication table: "))
multiplication_table(num)

# Second largest number
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

numbers_list = list(map(int, input("Enter numbers: ").split()))
second = second_largest(numbers_list)
print("Second largest number:", second if second is not None else "Not available")

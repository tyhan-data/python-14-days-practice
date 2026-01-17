# Day 5: If-Else Statements
# Task: Check even/odd, pass/fail

# Even or odd function
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

num = int(input("Enter a number: "))
print("Your number is:", even_odd(num))

# Pass/fail check
marks = float(input("Enter marks: "))
status = "Pass" if marks >= 50 else "Fail"
print("Student is:", status)

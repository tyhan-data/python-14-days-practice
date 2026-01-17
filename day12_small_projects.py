# Day 12: Small Projects
# Task: Calculator, Celsius to Fahrenheit, Grade check

# Calculator
def calculator(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

op = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Result:", calculator(op, num1, num2))

# Temperature converter
def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

temp = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", c_to_f(temp))

# Grade analysis
def marks_analysis(marks):
    grade_list = []
    for mark in marks:
        if 80 <= mark <= 100:
            grade_list.append("A+")
        elif 70 <= mark <= 79:
            grade_list.append("A")
        elif 60 <= mark <= 69:
            grade_list.append("A-")
        elif 50 <= mark <= 59:
            grade_list.append("B")
        elif 40 <= mark <= 49:
            grade_list.append("C")
        elif 0 < mark < 40:
            grade_list.append("F")
        else:
            grade_list.append("Invalid")
    return grade_list

marks_list = list(map(float, input("Enter student marks: ").split()))
print("Grades:", marks_analysis(marks_list))

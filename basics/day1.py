"""
Day 1 - Python Basics for DSA Journey

Topics Covered:
1. Variables
2. Arithmetic Operators
3. Relational Operators
4. Assignment Operators
5. Logical Operators
6. Type Casting
7. User Input
8. Basic Practice Problems
"""

# -------------------------------
# Variables and Basic Operations
# -------------------------------

a = 5
b = 2

print("Value of a:", a)
print("Value of b:", b)

# -------------------------------
# Arithmetic Operators
# -------------------------------

print("\nArithmetic Operations:")
print("Addition:", a + b)
print("Division:", a / b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# -------------------------------
# Relational Operators
# -------------------------------

print("\nRelational Operations:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a > b:", a > b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# -------------------------------
# Assignment Operators
# -------------------------------

num = 10
num **= 2

print("\nAssignment Operator Example:")
print("num after exponent operation:", num)

# -------------------------------
# Logical Operators
# -------------------------------

val1 = True
val2 = True

print("\nLogical Operations:")
print("NOT False:", not False)
print("NOT (a > b):", not (a > b))
print("AND Operator:", val1 and val2)
print("OR Operator:", val1 or val2)

# -------------------------------
# Type Casting
# -------------------------------

c = int("7")
d = 9

print("\nType Casting Example:")
print("c + d =", c + d)

# -------------------------------
# User Input
# -------------------------------

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("\nUser Details:")
print("Name:", name)
print("Age:", age)
print("Marks:", marks)

# -------------------------------
# Practice Problems
# -------------------------------

# Sum of two numbers
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Sum of numbers:", num1 + num2)

# Area of a square
side = int(input("\nEnter the side of the square: "))
print("Area of the square:", side * side)

# Average of two numbers
average = (num1 + num2) / 2
print("Average of numbers:", average)

# Comparison
print("Is num1 greater than or equal to num2?", num1 >= num2)
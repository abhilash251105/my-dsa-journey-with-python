# day2.py
# Day 2 - Python Practice
# Topics: Strings and Conditional Statements


# -------------------------------
# String Examples
# -------------------------------

str1 = "This is a string\nwe are creating it in Python"
print(str1)

first_name = "abhilash"
print(first_name)
print(len(first_name))

last_name = "tripathy"
print(last_name)
print(len(last_name))

final_string = first_name + " " + last_name
print(final_string)
print(len(final_string))


# -------------------------------
# String Slicing
# -------------------------------

name = "abhilashtripathy"
print(name[-4:len(name)])


# -------------------------------
# String Methods
# -------------------------------

text = "i am $learning python $from $$youtube"

print(text.endswith("Tube"))

text = text.capitalize()
print(text)

print(text.replace("n", "m"))

print(text.find("am"))

print(text.count("a"))

print("The number of $ symbol present:", text.count("$"))


# -------------------------------
# User Input Example
# -------------------------------

name_input = input("Enter your first name: ")
print("Your name length will be:", len(name_input))


# -------------------------------
# Conditional Statements
# -------------------------------

light = "red"

if light == "red":
    print("STOP")
elif light == "green":
    print("GO")
elif light == "yellow":
    print("LOOK")
else:
    print("Light is broken")

print("End of the code")


# -------------------------------
# Grade Calculator
# -------------------------------

marks = int(input("Enter the percentage you obtained: "))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "D"

print("The grade of the student is:", grade)


# -------------------------------
# Nested Condition
# -------------------------------

age = 34

if age >= 18:
    if age >= 70:
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")


# -------------------------------
# Even or Odd
# -------------------------------

num = int(input("Enter the number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# -------------------------------
# Largest of Three Numbers
# -------------------------------

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number:", num2)
else:
    print("Largest number:", num3)


# -------------------------------
# Multiple of 7
# -------------------------------

num = 12

if num % 7 == 0:
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")
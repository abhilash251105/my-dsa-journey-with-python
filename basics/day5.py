"""
Day 5 - Python Loops

Topics Covered:
1. While loops
2. For loops
3. Loop control (break, continue)
4. Range function
5. Searching in lists/tuples
6. Sum and factorial using loops
"""

# ---------------------------------
# While Loop Example
# ---------------------------------

count = 1

while count <= 5:
    print("Abhilash")
    count += 1

print("Loop finished. Final count:", count)

# ---------------------------------
# Print numbers from 5 to 1
# ---------------------------------

i = 5

while i >= 1:
    print(i)
    i -= 1

print("Countdown completed")

# ---------------------------------
# Print numbers from 1 to 100
# ---------------------------------

i = 1

while i <= 100:
    print(i)
    i += 1

print("Finished printing 1 to 100")

# ---------------------------------
# Print numbers from 100 to 1
# ---------------------------------

i = 100

while i >= 1:
    print(i)
    i -= 1

print("Finished printing 100 to 1")

# ---------------------------------
# Multiplication Table
# ---------------------------------

number = int(input("Enter a number for multiplication table: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

# ---------------------------------
# Traverse List using While Loop
# ---------------------------------

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1

# ---------------------------------
# Search Element in Tuple
# ---------------------------------

values = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

target = int(input("Enter the number to search: "))

index = 0

while index < len(values):
    if values[index] == target:
        print("Found at index:", index)
        break
    index += 1
else:
    print("Number not found")

# ---------------------------------
# Continue Example (Print Even Numbers)
# ---------------------------------

i = 1

while i <= 10:
    if i % 2 != 0:
        i += 1
        continue

    print("Even number:", i)
    i += 1

# ---------------------------------
# For Loop Example
# ---------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for num in numbers:
    if num == 4:
        print("Found 4")
        break
    print(num)
else:
    print("Loop finished")

print("End of program")

# ---------------------------------
# Print List using For Loop
# ---------------------------------

values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in values:
    print(num)

# ---------------------------------
# Search Element using For Loop
# ---------------------------------

tuple_values = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

target = int(input("Enter number to find: "))

for num in tuple_values:
    if num == target:
        print("Found:", num)

# ---------------------------------
# Multiplication Table using For Loop
# ---------------------------------

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number * i)

# ---------------------------------
# Sum of First N Numbers
# ---------------------------------

n = 5
total_sum = 0

for i in range(n + 1):
    total_sum += i

print("Sum of first", n, "numbers:", total_sum)

# ---------------------------------
# Sum using While Loop
# ---------------------------------

n = 5
total_sum = 0
i = 1

while i <= n:
    total_sum += i
    i += 1

print("Sum using while loop:", total_sum)

# ---------------------------------
# Factorial using For Loop
# ---------------------------------

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "is:", factorial)
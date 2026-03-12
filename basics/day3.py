"""
Day 3 - Python Lists and Tuples

Topics Covered:
1. List creation and indexing
2. List slicing
3. List methods
4. Tuple basics
5. User input with lists
6. Palindrome check using list
"""

# ---------------------------------
# List Creation and Access
# ---------------------------------

marks = [94.1, 85.6, 75.4, 66.5]

print("Marks List:", marks)
print("Type of marks:", type(marks))

print("First mark:", marks[0])
print("Second mark:", marks[1])

# ---------------------------------
# Mixed Data Types in List
# ---------------------------------

student = ["Abhilash", 98.1, 25, "Odisha"]

print("\nStudent List:", student)

# Changing value in list
student[0] = "Iresh"
print("Updated Student List:", student)

# List slicing
print("Marks from index 1 to 3:", marks[1:4])

# ---------------------------------
# List Methods
# ---------------------------------

numbers = [1, 3, 2, 4, 5]

numbers.append(6)
print("\nAfter append:", numbers)

numbers.sort()
print("Sorted list:", numbers)

numbers.sort(reverse=True)
print("Reverse sorted list:", numbers)

numbers.reverse()
print("List reversed:", numbers)

numbers.insert(1, 9)
print("After inserting 9 at index 1:", numbers)

numbers.remove(5)
print("After removing 5:", numbers)

numbers.pop(2)
print("After popping index 2:", numbers)

# ---------------------------------
# Tuple Basics
# ---------------------------------

tup = (1, 3, 2, 4, 5)
print("\nTuple:", tup)
print("Type of tuple:", type(tup))

# ---------------------------------
# User Input Example (Movies List)
# ---------------------------------

movies = []

movies.append(input("\nEnter first movie: "))
movies.append(input("Enter second movie: "))
movies.append(input("Enter third movie: "))

print("Favorite Movies:", movies)

# ---------------------------------
# Palindrome Check Using List
# ---------------------------------

values = [1, 2, 3]

copied_values = values.copy()
copied_values.reverse()

if copied_values == values:
    print("\nThe list is a Palindrome")
else:
    print("\nThe list is NOT a Palindrome")

# ---------------------------------
# Sorting Grades
# ---------------------------------

grades = ["A", "C", "D", "A", "E", "B"]

grades.sort()
print("\nSorted Grades:", grades)
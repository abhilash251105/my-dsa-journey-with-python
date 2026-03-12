"""
Day 4 - Python Dictionaries and Sets

Topics Covered:
1. Dictionary creation
2. Accessing dictionary elements
3. Dictionary methods (keys, values, items, get, update)
4. Nested dictionaries
5. Sets and set operations
6. User input stored in dictionary
"""

# ---------------------------------
# Dictionary Example
# ---------------------------------

info = {
    "name": ["Abhilash", "Piku", "Priya"],
    "age": ("25", "24", "19"),
    "study": "coding",
    "place": {
        "mkg": "752600",
        "klg": "752456",
        "dgri": "752458"
    }
}

print("Full Dictionary:", info)
print("Names:", info["name"])

print("\nDictionary Keys:", info.keys())
print("Dictionary Values:", info.values())
print("Dictionary Items:", info.items())

print("Using get() method:", info.get("name"))

# ---------------------------------
# Updating Dictionary
# ---------------------------------

new_dictionary = {
    "new": "one",
    "old": "two"
}

info.update(new_dictionary)

print("\nUpdated Dictionary:")
print(info)

# ---------------------------------
# Set Basics
# ---------------------------------

set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 8, 5, 4}

print("\nSet Operations")

print("Set1:", set1)
print("Set2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# ---------------------------------
# Dictionary with Mixed Values
# ---------------------------------

values = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "where we keep our books"]
}

print("\nDictionary Example:")
print(values)

# ---------------------------------
# Set Example (Unique Elements)
# ---------------------------------

languages = {
    "java", "python", "c++", "go", "java", "scala", "python", "scala"
}

print("\nUnique Programming Languages:")
print(languages)

print("Total unique languages:", len(languages))

# ---------------------------------
# User Input Example (Marks Dictionary)
# ---------------------------------

details = {}

english_marks = int(input("\nEnter marks for English: "))
details.update({"English": english_marks})

physics_marks = int(input("Enter marks for Physics: "))
details.update({"Physics": physics_marks})

print("\nStudent Marks Dictionary:")
print(details)

# ---------------------------------
# Set with Different Data Types
# ---------------------------------

mixed_values = {9, "9.0"}

print("\nSet with mixed values:", mixed_values)
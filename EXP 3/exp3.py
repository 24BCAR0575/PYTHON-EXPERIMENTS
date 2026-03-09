# WAP to display various string operations in Python

s = input("Enter a string: ")

print("Original String:", s)

# Length of string
print("Length of string:", len(s))

# Uppercase
print("Uppercase:", s.upper())

# Lowercase
print("Lowercase:", s.lower())

# Capitalize
print("Capitalized:", s.capitalize())

# Replace
print("Replace a with @:", s.replace('a','@'))

# String slicing
print("First 3 characters:", s[:3])
print("Last 3 characters:", s[-3:])

# Check substring
print("Contains 'python':", "python" in s)

# Count characters
print("Count of letter 'a':", s.count('a'))

# Find position
print("Position of first 'a':", s.find('a'))

# Reverse string
print("Reversed string:", s[::-1])
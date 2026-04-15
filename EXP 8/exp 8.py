import re

# The text we will analyze
text = "Contact us at support@example.com or sales@company.org for 24/7 help."

print(f"Original Text: {text}\n")

# 1. re.search() - Finds the first occurrence
# Pattern: \w+@\w+\.\w+ (Basic email pattern)
search_match = re.search(r"\w+@\w+\.\w+", text)
if search_match:
    print(f"1. Search Found: {search_match.group()}")

# 2. re.findall() - Finds all occurrences and returns a list
emails = re.findall(r"\w+@\w+\.\w+", text)
print(f"2. Find All (Emails): {emails}")

# 3. re.split() - Splits the string by a pattern
# Splitting by any whitespace
words = re.split(r"\s+", text)
print(f"3. Split into words: {words[:4]}...") # Showing first 4 words

# 4. re.sub() - Replaces matches with a new string
# Replacing digits with 'X'
hidden_numbers = re.sub(r"\d", "X", text)
print(f"4. Replace (Hidden Digits): {hidden_numbers}")

# 5. re.match() - Checks if the pattern is at the very START of the string
start_check = re.match(r"Contact", text)
print(f"5. Match at start: {'Yes' if start_check else 'No'}")
# Day 2: Strings & Methods
# Task:
# - Declare a string
# - Use .upper() and .lower()
# - Split the string into words
# - Join a list of words into a string

# 1️ Declare a string
my_string = "Hello Python"
print("Original string:", my_string)

# 2️ Convert to uppercase
upper_str = my_string.upper()
print("Uppercase:", upper_str)

# 3️ Convert to lowercase
lower_str = my_string.lower()
print("Lowercase:", lower_str)

# 4️ Split the string into words
words_list = my_string.split()
print("Split into words:", words_list)

# 5️ Join a list of words into a string
words = ["Hello", "Python", "World"]
joined_str = ' '.join(words)
print("Joined string:", joined_str)

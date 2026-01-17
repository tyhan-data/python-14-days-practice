# Day 9: String Problems
# Task:
# 1. Count vowels in a string
# 2. Reverse a string
# 3. Check if a string is a palindrome

# 1️ Function to count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

# 2️ Function to reverse a string
def reverse_string(s):
    return s[::-1]

# 3️ Function to check if a string is a palindrome
def is_palindrome(s):
    s_clean = s.replace(" ", "").lower()  # ignore spaces & case
    return s_clean == s_clean[::-1]


#  Testing the functions
user_input = input("Enter a string: ")

vowel_count = count_vowels(user_input)
reversed_str = reverse_string(user_input)
palindrome_check = is_palindrome(user_input)

print("\nResults:")
print("Number of vowels:", vowel_count)
print("Reversed string:", reversed_str)
print("Is palindrome?:", "Yes" if palindrome_check else "No")

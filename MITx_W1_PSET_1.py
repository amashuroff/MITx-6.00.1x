# Problem 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl'
#  your program should print: Number of vowels: 5
s = 'azcbobobegghakl'
vowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1
print('Number of vowels:', vowels)


# Problem 2
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2
counter = 0
for i in range(len(s)):
    if s[i:i + 3] == "bob":
        counter += 1
print('Number of times bob occurs is: ', counter)


# Problem 3
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example,
# if s = 'azcbobobegghakl', then your program should print: Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc
s = 'azcbobobegghakl'
current_str = s[0]
longest_str = s[0]
max_length = 0
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        current_str += s[i+1]
        if len(current_str) > max_length:
            max_length = len(current_str)
            longest_str = current_str
    else:
        current_str = s[i + 1]
print("The longest substring in alphabetical order is:" + longest_str)



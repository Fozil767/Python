#1)Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input('Foydalanuvchining ismini kiriting')
age = input('Foydalanuvchining yoshini kiriting')
letter = 'My name is {}, and I am {} years old'. format(name,age)
letter
#2)Extract car names from the following text:

txt = 'LMaasleitbtui'

txt[::2]
txt[1::2]

#3)Extract car names from the following text:

txt = 'MsaatmiazD'

txt[::2]
txt[-1::-2]

#4)Extract the residence area from the following text:

txt = "I'am John. I am from London"
import re

txt = "I'am John. I am from London"

# "I am from" dan keyingi so‘zni olish uchun regex
match = re.search(r'I am from ([A-Za-z]+)', txt)

if match:
    residence_area = match.group(1)
    print("Residence area:", residence_area)
else:
    print("Residence area not found.")

#5)Write a Python program that takes a user input string and prints it in reverse order.

# Take input from the user
user_input = input("Enter a string: ")

# Reverse the string using slicing
reversed_string = user_input[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)

#6. Count Vowels
#Write a Python program that counts the number of vowels in a given string.

# Take input from the user
user_input = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels using a loop
vowel_count = 0
for char in user_input:
    if char in vowels:
        vowel_count += 1

# Print the result
print("Number of vowels in the string:", vowel_count)

#7. Find Maximum Value
#Write a Python program that takes a list of numbers as input and prints the maximum value.
# Ask the user to input numbers separated by spaces
numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list and convert each to an integer
num_list = [int(num) for num in numbers.split()]

# Find the maximum value in the list
max_value = max(num_list)

# Print the result
print("The maximum value is:", max_value)

#8). Check Palindrome
#Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
# Ask the user to input a word
word = input("Enter a word: ")

# Convert the word to lowercase to make it case-insensitive
word = word.lower()

# Check if the word is equal to its reverse
if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

#9. Extract Email Domain
#Write a Python program that extracts and prints the domain from an email address provided by the user.
# Ask the user to input an email address
email = input("Enter your email address: ")

# Split the email at the '@' symbol and get the domain part
if "@" in email:
    domain = email.split("@")[1]
    print("The domain of the email is:", domain)
else:
    print("Invalid email address.")

#10. Generate Random Password
#Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

# Ask the user to specify the password length
length = int(input("Enter the desired password length: "))

# Define the characters to choose from
letters = string.ascii_letters
digits = string.digits
specials = string.punctuation

# Combine all characters
all_chars = letters + digits + specials

# Randomly choose characters and generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)

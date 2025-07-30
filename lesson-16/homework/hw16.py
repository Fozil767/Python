# 1)Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
# Raqamli qiymatlar ro'yxatini bir o'lchovli NumPy massiviga aylantirish uchun NumPy dasturini yozing.

import numpy as np

# Original list
original_list = [12.23, 13.32, 100, 36.32]

# Convert list to one-dimensional NumPy array
array = np.array(original_list)

# Print results
print("Original List:", original_list)
print("One-dimensional NumPy array:", array)

# 2)Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Qiymatlari 2 dan 10 gacha bo'lgan 3x3 matritsa yaratish uchun NumPy dasturini yozing.

import numpy as np

# Create array with values from 2 to 10 and reshape to 3x3
matrix = np.arange(2, 11).reshape(3, 3)

# Print the result
print(matrix)


# 3)Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# 10 o'lchamdagi null vektorni yaratish va oltinchi qiymatni 11 ga yangilash uchun NumPy dasturini yozing.

import numpy as np

# Create a null vector of size 10
vector = np.zeros(10)

# Display the original vector
print("Original vector:", vector)

# Update the sixth value (index 6) to 11
vector[6] = 11

# Display the updated vector
print("Updated vector:", vector)



# 4)Write a NumPy program to create an array with values ranging from 12 to 38.
# Qiymatlari 12 dan 38 gacha bo‘lgan massiv yaratish uchun NumPy dasturini yozing.

import numpy as np

# Create array with values from 12 to 37
array = np.arange(12, 38)

# Print the result
print(array)


# 5)Write a NumPy program to convert an array to a floating type.
# Massivni suzuvchi turga aylantirish uchun NumPy dasturini yozing.

import numpy as np

# Original integer array
original_array = np.array([1, 2, 3, 4])
print("Original array:", original_array)

# Convert to float type
float_array = original_array.astype(float)
print("Array converted to float type:", float_array)

# 6)Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Santigrad darajalarini Farengeyt darajalariga aylantirish uchun NumPy dasturini yozing. Santigrad qiymatlari NumPy massivida saqlanadi.
# Namuna massivi [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]

import numpy as np

# Centigrade values
centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

# Convert to Fahrenheit
fahrenheit = centigrade * 9/5 + 32

# Print results
print("Values in Centigrade degrees:", centigrade)
print("Values in Fahrenheit degrees:", fahrenheit)


# 7)Write a NumPy program to append values to the end of an array.
# Massiv oxiriga qiymatlarni qo'shish uchun NumPy dasturini yozing.

import numpy as np

# Original array
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

# Values to append
values_to_append = [40, 50, 60, 70, 80, 90]

# Append values to the original array
new_array = np.append(original_array, values_to_append)

# Print the updated array
print("After append values to the end of the array:", new_array)

# 8)Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
# 10 ta elementdan iborat tasodifiy NumPy massivi yarating va massivning o‘rtacha, mediana va standart og‘ishini hisoblang.

import numpy as np

# Create a random array of 10 elements
random_array = np.random.rand(10)  # Values between 0 and 1

# Calculate statistics
mean_val = np.mean(random_array)
median_val = np.median(random_array)
std_dev = np.std(random_array)

# Print results
print("Random Array:", random_array)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)


# 9)Create a 10x10 array with random values and find the minimum and maximum values.
# Tasodifiy qiymatlar bilan 10x10 massiv yarating va minimal va maksimal qiymatlarni toping.

import numpy as np

# Create a 10x10 array with random values between 0 and 1
random_array = np.random.rand(10, 10)

# Find the minimum and maximum values
min_val = np.min(random_array)
max_val = np.max(random_array)

# Print the array and results
print("Random 10x10 Array:\n", random_array)
print("\nMinimum value:", min_val)
print("Maximum value:", max_val)


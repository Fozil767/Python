import pandas as pd
import numpy as np

# Original data
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

# Create DataFrame
df = pd.DataFrame(data)

# Rename columns using a function
df.rename(columns=lambda x: x.lower().replace(" ", "_"), inplace=True)

# Print the first 3 rows
print("First 3 rows:")
print(df.head(3), "\n")

# Find the mean age
mean_age = df['age'].mean()
print("Mean age:", mean_age, "\n")

# Select and print only 'first_name' and 'city' columns
print("Name and City columns:")
print(df[['first_name', 'city']], "\n")

# Add a new column 'salary' with random salary values between 50,000 and 100,000
df['salary'] = np.random.randint(50000, 100001, size=len(df))

# Display summary statistics of the DataFrame
print("Summary statistics:")
print(df.describe())


import pandas as pd

# Ma'lumotlar
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

# DataFrame yaratish
sales_and_expenses = pd.DataFrame(data)

# DataFrame ni chiqarish
print("Sales and Expenses DataFrame:")
print(sales_and_expenses, "\n")

# Maksimal qiymatlar
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("Maksimal sotuv:", max_sales)
print("Maksimal xarajat:", max_expenses, "\n")

# Minimal qiymatlar
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("Minimal sotuv:", min_sales)
print("Minimal xarajat:", min_expenses, "\n")

# O‘rtacha qiymatlar
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("O‘rtacha sotuv:", avg_sales)
print("O‘rtacha xarajat:", avg_expenses)


import pandas as pd

# Ma'lumotlar
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data)

# 'Category' ustunini indeksga aylantirish
expenses.set_index('Category', inplace=True)

# DataFrame ni ko'rish
print("Xarajatlar jadvali:\n", expenses, "\n")

# Maksimal xarajatlar (har bir kategoriya uchun)
max_expenses = expenses.max(axis=1)
print("Maksimal xarajatlar:\n", max_expenses, "\n")

# Minimal xarajatlar (har bir kategoriya uchun)
min_expenses = expenses.min(axis=1)
print("Minimal xarajatlar:\n", min_expenses, "\n")

# O‘rtacha xarajatlar (har bir kategoriya uchun)
avg_expenses = expenses.mean(axis=1)
print("O‘rtacha xarajatlar:\n", avg_expenses)

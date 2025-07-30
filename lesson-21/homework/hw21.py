import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Har bir talabaning o'rtacha bahosini hisoblash
df1["Average_Grade"] = df1[["Math", "English", "Science"]].mean(axis=1)

# Natijani ko‘rish
print(df1)
# Avvalgi koddan foydalanib, har bir talabaga o'rtacha baho hisoblangan bo'lishi kerak
# Agar hisoblanmagan bo‘lsa, quyidagicha qo‘shing:
df1["Average_Grade"] = df1[["Math", "English", "Science"]].mean(axis=1)

# Eng yuqori o‘rtacha bahoga ega talaba
top_student = df1.loc[df1["Average_Grade"].idxmax()]

# Natijani chiqarish
print("Eng yuqori o‘rtacha bahoga ega talaba:")
print(top_student)


# 'Total' ustunini qo'shish (Math + English + Science)
df1["Total"] = df1[["Math", "English", "Science"]].sum(axis=1)

# Natijani chiqarish
print(df1)


# Har bir mahsulot bo'yicha umumiy savdo hajmi
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

total_sales = df2[["Product_A", "Product_B", "Product_C"]].sum()

# Natijani chiqarish
print("Har bir mahsulot bo'yicha umumiy savdo hajmi:\n")
print(total_sales)


# Har bir kun uchun umumiy savdoni hisoblash
# Har bir mahsulot bo'yicha umumiy savdo hajmi
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

df2["Total_Sales"] = df2[["Product_A", "Product_B", "Product_C"]].sum(axis=1)

# Eng yuqori savdo bo‘lgan sanani topish
max_sales_date = df2.loc[df2["Total_Sales"].idxmax(), "Date"]

# Natijani chiqarish
print("Eng ko‘p savdo bo‘lgan sana:", max_sales_date)


# Har bir mahsulot uchun kunlik foiz o‘zgarishini hisoblash
percentage_change = df2[["Product_A", "Product_B", "Product_C"]].pct_change() * 100

# Natijani yaxlitlab chiqaramiz
percentage_change = percentage_change.round(2)

# Natijani chiqarish
print("Kunlik foiz o‘zgarishlari (%):\n")
print(percentage_change)


import matplotlib.pyplot as plt

# Grafikka o‘lcham berish
plt.figure(figsize=(10, 6))

# Har bir mahsulot uchun chiziq chizish
plt.plot(df2["Date"], df2["Product_A"], label="Product A", marker='o')
plt.plot(df2["Date"], df2["Product_B"], label="Product B", marker='s')
plt.plot(df2["Date"], df2["Product_C"], label="Product C", marker='^')

# Grafik elementlarini sozlash
plt.title("Mahsulotlar bo‘yicha kunlik savdo trendi")
plt.xlabel("Sana")
plt.ylabel("Savdo miqdori")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Grafikni chiqarish
plt.tight_layout()
plt.show()

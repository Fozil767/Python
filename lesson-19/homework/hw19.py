import pandas as pd

# CSV faylni o'qish
df = pd.read_csv("task/sales_data.csv", parse_dates=['Date'])

# Birinchi 5 qatordan namuna
print("📌 Dastlabki ma'lumotlar:\n", df.head(), "\n")



df['Total_Revenue'] = df['Quantity'] * df['Price']

revenue_by_category = df.groupby('Category')['Total_Revenue'].sum()
print("📌 Kategoriya bo‘yicha jami daromad:\n", revenue_by_category, "\n")


top_product = df.groupby('Product')['Total_Revenue'].sum().sort_values(ascending=False).head(1)
print("📌 Eng ko‘p daromad keltirgan mahsulot:\n", top_product, "\n")


daily_revenue = df.groupby('Date')['Total_Revenue'].sum()
print("📌 Har kuni bo‘yicha daromad:\n", daily_revenue, "\n")

top_selling_category = df.groupby('Category')['Quantity'].sum().sort_values(ascending=False).head(1)
print("📌 Eng ko‘p sotilgan kategoriya:\n", top_selling_category, "\n")

df.to_excel("task\\sales_data_with_total.xlsx", index=False)
print("✅ Jadval 'sales_data_with_total.xlsx' faylga saqlandi.")


import pandas as pd

# Faylni o'qish
df = pd.read_csv("task\\sales_data.csv", parse_dates=["Date"])

# Total Revenue ustunini qo‘shish
df["Total_Revenue"] = df["Quantity"] * df["Price"]

# 1. Group by Category va kerakli statistikalarni hisoblash
category_stats = df.groupby("Category").agg(
    total_quantity_sold=("Quantity", "sum"),
    avg_price_per_unit=("Price", "mean"),
    max_quantity_in_one_transaction=("Quantity", "max")
)

print("📊 Category bo‘yicha agregat statistikalar:\n")
print(category_stats, "\n")

# 2. Har bir kategoriya bo‘yicha eng ko‘p sotilgan mahsulotni aniqlash
top_products = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()

# Har bir kategoriya bo‘yicha eng ko‘p quantity bilan mahsulot tanlash
top_selling_by_category = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False]) \
                                      .drop_duplicates('Category')

print("🏆 Har bir kategoriya bo‘yicha eng ko‘p sotilgan mahsulot:\n")
print(top_selling_by_category[["Category", "Product", "Quantity"]], "\n")

# 3. Eng yuqori umumiy savdo (quantity * price) qilingan sanani aniqlash
daily_sales = df.groupby("Date")["Total_Revenue"].sum()
max_sales_date = daily_sales.idxmax()
max_sales_amount = daily_sales.max()

print(f"📅 Eng yuqori savdo amalga oshirilgan sana: {max_sales_date.date()} (${max_sales_amount:.2f})")


import pandas as pd

# Ma'lumotni o'qish
df = pd.read_csv("task\\customer_orders.csv")

# Total qiymat qo'shish (Quantity * Price)
df["TotalAmount"] = df["Quantity"] * df["Price"]

# Ma'lumotlar namunasi
print("📌 Dastlabki qatorlar:\n", df.head(), "\n")




  

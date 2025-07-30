import pandas as pd

# 1. Load the data
df = pd.read_csv("task\\customer_orders.csv")

# 2. Create a column for total price per order
df["TotalPrice"] = df["Quantity"] * df["Price"]

# 3. Group by CustomerID and sum up TotalPrice
total_spent = df.groupby("CustomerID")["TotalPrice"].sum().reset_index()

# 4. Rename column for clarity
total_spent.columns = ["CustomerID", "TotalAmountSpent"]

# 5. Sort descending (optional)
total_spent = total_spent.sort_values(by="TotalAmountSpent", ascending=False)

# 6. Display result
print(total_spent)


import pandas as pd

# 1. Load the dataset
df = pd.read_csv("task\\customer_orders.csv")

# 2. Calculate total price per order
df["TotalPrice"] = df["Quantity"] * df["Price"]

# 3. Group by CustomerID and sum total prices
total_spent = df.groupby("CustomerID")["TotalPrice"].sum().reset_index()

# 4. Rename column
total_spent.columns = ["CustomerID", "TotalAmountSpent"]

# 5. Sort in descending order
top_customers = total_spent.sort_values(by="TotalAmountSpent", ascending=False)

# 6. Select top 5 customers
top_5_customers = top_customers.head(5)

# 7. Display result
print("🔝 Top 5 Customers by Total Purchase Amount:")
print(top_5_customers)


import pandas as pd

# 1. Load orders and customers data
orders_df = pd.read_csv("task\\customer_orders.csv")
customers_df = pd.read_csv("task\\customers.csv")  # Assumed to have 'CustomerID' and 'CustomerName'

# 2. Calculate total price per order
orders_df["TotalPrice"] = orders_df["Quantity"] * orders_df["Price"]

# 3. Calculate total amount spent per customer
total_spent = orders_df.groupby("CustomerID")["TotalPrice"].sum().reset_index()
total_spent.columns = ["CustomerID", "TotalAmountSpent"]

# 4. Merge with customer names
merged = pd.merge(total_spent, customers_df, on="CustomerID")

# 5. Sort and get top 5 customers
top_5 = merged.sort_values(by="TotalAmountSpent", ascending=False).head(5)

# 6. Select and display the desired columns
top_5 = top_5[["CustomerID", "CustomerName", "TotalAmountSpent"]]
print("🔝 Top 5 Customers by Total Amount Spent:")
print(top_5)



import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("task\\population.db")  # or actual music db

# Load data via SQL
invoice_lines = pd.read_sql_query("SELECT InvoiceId, TrackId FROM InvoiceLine", conn)
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM Invoice", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)

# Merge to get full mapping: CustomerId - AlbumId - TrackId
df = invoice_lines.merge(invoices, on="InvoiceId").merge(tracks, on="TrackId")

# Tracks bought by customer per album
customer_album_track_counts = df.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index()
customer_album_track_counts.columns = ["CustomerId", "AlbumId", "TracksBought"]

# Total tracks per album
total_tracks_per_album = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index()
total_tracks_per_album.columns = ["AlbumId", "TotalTracks"]

# Merge both
merged = customer_album_track_counts.merge(total_tracks_per_album, on="AlbumId")

# Determine if full album was purchased
merged["FullAlbumBought"] = merged["TracksBought"] == merged["TotalTracks"]

# For each customer, check if they ever bought a full album
customer_pref = merged.groupby("CustomerId")["FullAlbumBought"].any().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbumBought"].apply(lambda x: "Full Album" if x else "Individual Tracks")

# Summary
summary = customer_pref["Preference"].value_counts(normalize=True) * 100
print("🎧 Customer Preferences (%):")
print(summary.round(2))



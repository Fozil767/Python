# 1)Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
#Roster nomli jadval bilan yangi ma'lumotlar bazasini yarating, unda uchta maydon mavjud: Ism, Tur va Yosh. Ism va Tur ustunlari matn maydonlari, Yosh ustuni esa butun son maydoni bo'lishi kerak.

import sqlite3

# Yangi SQLite ma'lumotlar bazasini yaratish
conn = sqlite3.connect("zoo_database.db")
cursor = conn.cursor()

# Roster jadvalini yaratish
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# O'zgarishlarni saqlash
conn.commit()
conn.close()

print("✅ Roster jadvali yaratildi.")



# 2)Populate your new table with the following values:
#Yangi jadvalingizni quyidagi qiymatlar bilan to'ldiring:

import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect("zoo_database.db")
cursor = conn.cursor()

# Ma'lumotlarni qo‘shish
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

# O‘zgarishlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

print("✅ Ma'lumotlar Roster jadvaliga muvaffaqiyatli qo‘shildi.")

#3)Update the Name of Jadzia Dax to be Ezri Dax

import sqlite3

conn = sqlite3.connect("zoo_database.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

conn.commit()
conn.close()

print("✅ Jadzia Dax ismi Ezri Dax ga o‘zgartirildi.")

#4)Display the Name and Age of everyone in the table classified as Bajoran.
#Jadvalda Bajoran deb tasniflangan har bir kishining ismi va yoshini ko'rsating.

import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('zoo_database.db')  # yoki .sqlite, .db nomi ixtiyoriy
cursor = conn.cursor()

# So‘rov: Bajoran bo‘lganlar
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()

# Natijani chiqarish
for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")

# Ulanishni yopish
conn.close()

mevalar = {
    'olma': 5,
    'banan': 2,
    'gilos': 7,
    'xurmo': 1
}

# Oshish tartibida (ascending)
asc = dict(sorted(mevalar.items(), key=lambda meva: meva[1]))
print("Oshish tartibi:", asc)

# Kamayish tartibida (descending)
desc = dict(sorted(mevalar.items(), key=lambda meva: meva[1], reverse=True))
print("Kamayish tartibi:", desc)

#2)Write a Python script to add a key to a dictionary. Lug'atga kalit qo'shish uchun Python skriptini yozing.


my_dict = {0: 10, 1: 20}

# ✅ Yangi kalit 2, qiymati 30
my_dict[2] = 30

print(my_dict)

#3)Write a Python script to concatenate the following dictionaries to create a new one.Yangi lug'at yaratish uchun quyidagi lug'atlarni birlashtirish uchun Python skriptini yozing.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Bo'sh yangi lug‘at yaratamiz
new_dict = {}

# Har bir lug‘atni qo‘shamiz
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print("Yangi birlashtirilgan lug‘at:", new_dict)
#4)Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#(x, x*x) ko'rinishida raqamni (1 va n oralig'ida) o'z ichiga olgan lug'at yaratish va chop etish uchun Python skriptini yozing.

# Foydalanuvchidan n sonini so‘raymiz
n = int(input("n ni kiriting: "))

# Bo‘sh lug‘at yaratamiz
kvadratlar = {}

# 1 dan n gacha har bir sonni kvadratini hisoblaymiz
for x in range(1, n + 1):
    kvadratlar[x] = x * x

# Natijani chiqaramiz
print("Natija:", kvadratlar)


#5)Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Lug'atni chop etish uchun Python skriptini yozing, bu erda kalitlar 1 dan 15 gacha bo'lgan raqamlar (ikkalasi ham kiritilgan) va qiymatlar kalitlarning kvadratidir.

# Bo'sh lug‘at yaratamiz
kvadratlar = {}

# 1 dan 15 gacha bo'lgan sonlar uchun
for x in range(1, 16):
    kvadratlar[x] = x * x

# Natijani chiqaramiz
print(kvadratlar)

#6)Write a Python program to create a set. To'plam yaratish uchun Python dasturini yozing.
my_set = {1, 2, 3, 4, 5}
print("To‘plam:", my_set)

#7)Write a Python program to iterate over sets.To'plamlarni takrorlash uchun Python dasturini yozing.

my_set = {"olma", "banan", "gilos", "xurmo"}

print("To‘plamdagi elementlar:")
for meva in my_set:
    print(meva)

#8)Write a Python program to add member(s) to a set.To'plamga a'zo(lar)ni qo'shish uchun Python dasturini yozing.
my_set = {"olma", "banan"}

# Bitta element qo‘shamiz
my_set.add("gilos")

print("Yangi to‘plam:", my_set)

#9)Write a Python program to remove item(s) from a given set.Berilgan to'plamdan element(lar)ni olib tashlash uchun Python dasturini yozing.
my_set = {"olma", "banan", "gilos"}

# "banan" elementini olib tashlash
my_set.remove("banan")

print("To‘plamdan keyin:", my_set)


#10)Write a Python program to remove an item from a set if it is present in the set.Agar to'plamda mavjud bo'lsa, to'plamdan elementni olib tashlash uchun Python dasturini yozing.

# To‘plam (set) yaratiladi
my_set = {"olma", "banan", "gilos"}

# O‘chirilmoqchi bo‘lgan element
item = "banan"

# Tekshirib, bor bo‘lsa o‘chiramiz
if item in my_set:
    my_set.remove(item)
    print(f"'{item}' o‘chirildi.")
else:
    print(f"'{item}' to‘plamda mavjud emas.")

# Natijani chiqaramiz
print("Yangi to‘plam:", my_set)


#1)Create a list containing five different fruits and print the third fruit.

# Mevalar ro'yxatini yaratamiz
mevalar = ["Olma", "Banan", "Gilos", "Apelsin", "Mango"]

# Uchinchi mevani chop etamiz (ro'yxat indekslari 0 dan boshlanadi, 0 - 1 - 2...)
print("Uchinchi meva bu:", mevalar[2])

#2)Create two lists of numbers and concatenate them into a single list.

# Birinchi raqamlar ro'yxati
raqamlar1 = [1, 2, 3]

# Ikkinchi raqamlar ro'yxati
raqamlar2 = [4, 5, 6]

# Ikkala ro'yxatni birlashtiramiz
barcha_raqamlar = raqamlar1 + raqamlar2

# Natijani chop etamiz
print("Yangi birlashtirilgan ro'yxat:", barcha_raqamlar)

#3)Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

# Asosiy ro'yxat
raqamlar = [10, 20, 30, 40, 50, 60, 70]

# Birinchi element
birinchi = raqamlar[0]

# O'rta element (ro'yxat uzunligining yarmi)
orta = raqamlar[len(raqamlar) // 2]

# Oxirgi element
oxirgi = raqamlar[-1]

# Yangi ro'yxatga saqlaymiz
yangi_royxat = [birinchi, orta, oxirgi]

# Natijani chop etamiz
print("Yangi ro'yxat:", yangi_royxat)
#4)Create a list of your five favorite movies and convert it into a tuple.
# 5 ta sevimli kinolar ro'yxati
kinolar = ["Inception", "Interstellar", "The Dark Knight", "Avengers: Endgame", "Forrest Gump"]

# Ro'yxatni tuple (o'zgarmas to'plam) ga aylantiramiz
kino_tuple = tuple(kinolar)

# Natijani chop etamiz
print("Kinolar ro'yxati (tuple shaklida):", kino_tuple)

#5)Given a list of cities, check if "Paris" is in the list and print the result.

# Shaharlar ro'yxati
shaharlar = ["Toshkent", "London", "New York", "Paris", "Tokyo"]

# "Paris" ro'yxatda borligini tekshiramiz
natija = "Paris" in shaharlar

# Natijani chop etamiz
print("Paris ro'yxatda bormi?:", natija)

#6)Create a list of numbers and duplicate it without using loops.
# Raqamlar ro'yxati
raqamlar = [1, 2, 3, 4, 5]

# Ro'yxatni ikki marta takrorlaymiz (duplikatsiya qilamiz)
yangi_royxat = raqamlar * 2

# Natijani chop etamiz
print("Takrorlangan ro'yxat:", yangi_royxat)

#7)Given a list of numbers, swap the first and last elements.
# Raqamlar ro'yxati
raqamlar = [10, 20, 30, 40, 50]

# Birinchi va oxirgi elementlarni almashtiramiz
raqamlar[0], raqamlar[-1] = raqamlar[-1], raqamlar[0]

# Natijani chop etamiz
print("O'zgartirilgan ro'yxat:", raqamlar)

#8)Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
# 1 dan 10 gacha bo'lgan sonlar bilan tuple yaratamiz
sonlar = tuple(range(1, 11))

# 3-chi indeksdan (4-element) 7-chi indeksgacha bo'lgan bo'lakni kesib olamiz
qirqim = sonlar[3:8]  # 8 kirmaydi, ya'ni 3,4,5,6,7-chi indekslar olinadi

# Natijani chop etamiz
print("Kesilgan qism:", qirqim)


#9)Create a list of colors and count how many times "blue" appears in the list.
# Ranglar ro'yxati
ranglar = ["red", "blue", "green", "blue", "yellow", "blue"]

# "blue" so'zining nechta marta qatnashganini hisoblaymiz
blue_soni = ranglar.count("blue")

# Natijani chop etamiz
print('"blue" ro\'yxatda nechta marta bor:', blue_soni)


#10)Given a tuple of animals, find the index of "lion".
# Hayvonlar tuple'i
hayvonlar = ("cat", "dog", "lion", "tiger", "elephant")

# "lion" elementining indeksini topamiz
lion_index = hayvonlar.index("lion")

# Natijani chop etamiz
print('"lion" ning indeksi:', lion_index)


#11)Create two tuples of numbers and merge them into a single tuple.
# Birinchi tuple
sonlar1 = (1, 2, 3)

# Ikkinchi tuple
sonlar2 = (4, 5, 6)

# Ikkala tuple ni birlashtiramiz
birlashtirilgan = sonlar1 + sonlar2

# Natijani chop etamiz
print("Yagona tuple:", birlashtirilgan)

#12)Given a list and a tuple, find and print their lengths.
# Ro'yxat (list)
mevalar = ["olma", "banan", "gilos", "nok"]

# Tuple
hayvonlar = ("mushuk", "it", "qush")

# Ro'yxatning uzunligini topamiz
uzunlik_list = len(mevalar)

# Tuple ning uzunligini topamiz
uzunlik_tuple = len(hayvonlar)

# Natijalarni chop etamiz
print("Ro'yxat (list) uzunligi:", uzunlik_list)
print("Tuple uzunligi:", uzunlik_tuple)


#13)Create a tuple of five numbers and convert it into a list
# 5 ta sondan iborat tuple
sonlar_tuple = (10, 20, 30, 40, 50)

# Tuple ni list ga aylantiramiz
sonlar_list = list(sonlar_tuple)

# Natijani chop etamiz
print("Tuple:", sonlar_tuple)
print("List:", sonlar_list)

#14)Given a tuple of numbers, find and print the maximum and minimum values.
# Raqamlardan iborat tuple
sonlar = (12, 45, 7, 89, 23, 5, 67)

# Eng katta va eng kichik qiymatlarni topamiz
eng_katta = max(sonlar)
eng_kichik = min(sonlar)

# Natijalarni chop etamiz
print("Eng katta son:", eng_katta)
print("Eng kichik son:", eng_kichik)

#15)Create a tuple of words and print it in reverse order.
# So'zlardan iborat tuple
sozlar = ("salom", "dunyo", "python", "o'rganamiz", "birga")

# Tuple ni teskari tartibda chiqaramiz
teskari = sozlar[::-1]

# Natijani chop etamiz
print("Teskari tartibda tuple:", teskari)




#1)Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
#Raqamni nolga bo'lishda ZeroDivisionError istisnosini boshqarish uchun Python dasturini yozing.

try:
    numerator = int(input("Suratni kiriting (ya'ni bo‘linuvchi son): "))
    denominator = int(input("Maxrajni kiriting (ya'ni bo‘luvchi son): "))
    result = numerator / denominator
    print("Natija:", result)

except ZeroDivisionError:
    print("Xatolik: 0 ga bo‘lish mumkin emas.")

except ValueError:
    print("Xatolik: Raqam kiriting, harf emas.")

#2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
#Foydalanuvchini butun sonni kiritishni taklif qiladigan va agar kiritilgan butun son bo'lmasa, ValueError istisnosini ko'taradigan Python dasturini yozing.

try:
    user_input = input("Iltimos, butun son kiriting: ")
    number = int(user_input)  # Bu yerda xato chiqishi mumkin
    print("Siz kiritgan son:", number)

except ValueError:
    raise ValueError("Xatolik: Siz butun son kiritmadingiz!")

#3)Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
#Faylni ochadigan va fayl mavjud bo'lmasa FileNotFoundError istisnosini boshqaradigan Python dasturini yozing.

try:
    file_name = input("Fayl nomini kiriting (masalan: data.txt): ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except FileNotFoundError:
    print(f"Xatolik: '{file_name}' nomli fayl topilmadi.")

#4)Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
#Foydalanuvchiga ikkita raqam kiritishni taklif qiladigan va agar kirishlar sonli bo'lmasa, TypeError istisnosini keltirib chiqaradigan Python dasturini yozing.

try:
    a = input("Birinchi sonni kiriting: ")
    b = input("Ikkinchi sonni kiriting: ")

    # Kiritilgan qiymatlar son emasligini tekshiramiz
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Faqat son kiriting!")

    # Agar son bo‘lsa, float() ga aylantiramiz
    a = float(a)
    b = float(b)

    print(f"Ikkala son yig'indisi: {a + b}")

except TypeError as e:
    print(f"Xatolik: {e}")

#5)Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
#Agar ruxsat berish muammosi bo'lsa, faylni ochadigan va PermissionError istisnosini boshqaradigan Python dasturini yozing.

try:
    # Ruxsatsiz (read-only yoki boshqa himoyalangan) faylga yozishga urinish
    with open("protected_file.txt", "w") as file:
        file.write("Bu faylga yozishga harakat qilinmoqda.")
    print("Fayl muvaffaqiyatli yozildi.")

except PermissionError:
    print("Xatolik: Faylga yozish uchun ruxsat yo'q (PermissionError).")

#6)Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
#Ro'yxatda amalni bajaradigan va indeks diapazondan tashqarida bo'lsa, IndexError istisnosini boshqaradigan Python dasturini yozing.

try:
    my_list = [10, 20, 30, 40, 50]
    index = int(input("Nechanchi indeksdagi elementni ko'rsatmoqchisiz? (0 dan boshlab): "))
    print("Tanlangan element:", my_list[index])

except IndexError:
    print("Xatolik: Indeks ro'yxat doirasidan tashqarida (IndexError).")

except ValueError:
    print("Xatolik: Iltimos, faqat butun son kiriting.")

#7)Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
#Foydalanuvchiga raqam kiritishni taklif qiladigan va agar foydalanuvchi kiritishni bekor qilsa, KeyboardInterrupt istisnosini boshqaradigan Python dasturini yozing.

try:
    number = int(input("Iltimos, biror son kiriting: "))
    print("Siz kiritgan son:", number)

except KeyboardInterrupt:
    print("\nXatolik: Kiritish bekor qilindi (KeyboardInterrupt).")

except ValueError:
    print("Xatolik: Iltimos, faqat butun son kiriting.")


#8)Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
#Agar arifmetik xato bo'lsa, bo'linishni bajaradigan va ArithmeticError istisnosini boshqaradigan Python dasturini yozing.

try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print("Natija:", result)

except ArithmeticError as e:
    print("Arifmetik xatolik yuz berdi:", e)

except ValueError:
    print("Iltimos, faqat son kiriting.")


#8.1 Write a Python program to read an entire text file.
#Butun matn faylini o'qish uchun Python dasturini yozing.

try:
    with open("file.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)

except FileNotFoundError:
    print("Xatolik: 'file.txt' nomli fayl topilmadi.")

def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print(f"Xatolik: '{filename}' nomli fayl topilmadi.")

# Foydalanuvchidan fayl nomi va n sonini olish
filename = input("Fayl nomini kiriting (masalan: file.txt): ")
try:
    n = int(input("Nechta qatordan boshlab o‘qilsin (n): "))
    read_first_n_lines(filename, n)
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting.")


#8.3 Write a Python program to append text to a file and display the text.
#Faylga matn qo'shish va matnni ko'rsatish uchun Python dasturini yozing.

def append_and_display(filename, text):
    try:
        # 1. Faylga matn qo‘shish ('a' - append mode)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text + '\n')

        # 2. Faylni o‘qib, ekranga chiqarish
        print("\nFayldagi matn:")
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

    except Exception as e:
        print("Xatolik:", e)

# Foydalanuvchidan fayl nomi va matn so‘raladi
filename = input("Fayl nomini kiriting (masalan: file.txt): ")
text = input("Faylga qo‘shiladigan matnni kiriting: ")

append_and_display(filename, text)



 1)Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.
# Vazifa: JSON tahlili
# student.jon JSON faylini o'qiydigan va har bir talabaning tafsilotlarini chop etadigan Python skriptini yozing.

import json

# Fayl nomi
filename = 'students.json'

try:
    # JSON faylni ochish va o‘qish
    with open(filename, 'r', encoding='utf-8') as file:
        students = json.load(file)

    # Har bir talaba ma'lumotlarini chiqarish
    for student in students:
        print("🧑‍🎓 Talaba:")
        print(f"🆔 ID: {student['id']}")
        print(f"👤 Ismi: {student['name']}")
        print(f"🎂 Yoshi: {student['age']}")
        print(f"📘 Yo'nalishi: {student['major']}")
        print("-" * 30)

except FileNotFoundError:
    print(f"❌ Fayl topilmadi: {filename}")
except json.JSONDecodeError:
    print("❌ JSON formatida xatolik bor.")

#2) Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
# Vazifa: Ob-havo API
# Ushbu urldan foydalaning: https://openweathermap.org/
# Muayyan shahar (masalan, siz tug'ilgan shahar: Toshkent) uchun ob-havo ma'lumotlarini olish va tegishli ma'lumotlarni (harorat, namlik va boshqalar) chop etish uchun so'rovlar kutubxonasidan foydalaning.

import requests

# O'zgaruvchilar
API_KEY = "208ba2513564d4018ad59e91fe35b769"  # << o‘zingizning API kalitingizni bu yerga yozing
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# API so‘rovi
response = requests.get(url)

# Javobni tekshirish va chiqarish
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"🌤 Ob-havo Toshkentda:")
    print(f"📝 Holati: {weather}")
    print(f"🌡 Harorat: {temp}°C")
    print(f"🥵 His qilinadigan: {feels_like}°C")
    print(f"💧 Namlik: {humidity}%")
    print(f"🌬 Shamol tezligi: {wind_speed} m/s")
else:
    print("❌ Ob-havo ma'lumotlarini olishda xatolik yuz berdi.")


# 3)Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
# Vazifa: JSON modifikatsiyasi
# Foydalanuvchilarga yangi kitoblar qoʻshish, mavjud kitob maʼlumotlarini yangilash va books.json JSON faylidan kitoblarni oʻchirish imkonini beruvchi dastur yozing.


import json

def load_books(filename):
    """Fayldan kitoblar ro'yxatini o'qish."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            books = json.load(f)
    except FileNotFoundError:
        books = []  # Agar fayl topilmasa, bo'sh ro'yxat qaytaramiz
    return books

def save_books(filename, books):
    """Kitoblar ro'yxatini faylga yozish."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4, ensure_ascii=False)

def add_book(books):
    """Yangi kitob qo'shish."""
    print("\nYangi kitob qo'shish:")
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = input("Chop etilgan yil: ")
    
    # Agar mavjud kitoblar bo'lsa, eng katta id qiymatini oshirib ketamiz, aks holda id = 1
    new_id = max([book.get('id', 0) for book in books], default=0) + 1
    new_book = {"id": new_id, "title": title, "author": author, "year": year}
    books.append(new_book)
    print("✅ Kitob muvaffaqiyatli qo'shildi.\n")
    return books

def update_book(books):
    """Mavjud kitob ma'lumotlarini yangilash."""
    print("\nKitob ma'lumotlarini yangilash:")
    try:
        book_id = int(input("Yangilash uchun kitob ID sini kiriting: "))
    except ValueError:
        print("❌ ID son bo'lishi kerak!")
        return books

    for book in books:
        if book.get('id') == book_id:
            print("Joriy ma'lumotlar:", book)
            new_title = input("Yangi nom (qoldiring agar o'zgarmasin): ")
            new_author = input("Yangi muallif (qoldiring agar o'zgarmasin): ")
            new_year = input("Yangi yil (qoldiring agar o'zgarmasin): ")
            if new_title.strip():
                book['title'] = new_title
            if new_author.strip():
                book['author'] = new_author
            if new_year.strip():
                book['year'] = new_year
            print("✅ Kitob yangilandi.")
            return books
    print("❌ ID {0} li kitob topilmadi.".format(book_id))
    return books

def delete_book(books):
    """Kitobni ro'yxatdan o'chirish."""
    print("\nKitobni o'chirish:")
    try:
        book_id = int(input("O'chirish uchun kitob ID sini kiriting: "))
    except ValueError:
        print("❌ ID son bo'lishi kerak!")
        return books

    for index, book in enumerate(books):
        if book.get('id') == book_id:
            print("O'chirilayotgan kitob:", book)
            del books[index]
            print("✅ Kitob o'chirildi.")
            return books
    print("❌ ID {0} li kitob topilmadi.".format(book_id))
    return books

def list_books(books):
    """Barcha kitoblarni chiqarish."""
    print("\n📚 Kitoblar ro'yxati:")
    if not books:
        print("Hech qanday kitob mavjud emas.")
        return
    for book in books:
        print(f"ID: {book.get('id')}, Nom: {book.get('title')}, Muallif: {book.get('author')}, Yil: {book.get('year')}")

def main():
    filename = "books.json"
    books = load_books(filename)

    while True:
        print("\n=== Kitoblar Boshqaruvi ===")
        print("1. Yangi kitob qo'shish")
        print("2. Kitob ma'lumotlarini yangilash")
        print("3. Kitobni o'chirish")
        print("4. Barcha kitoblarni ko'rsatish")
        print("5. Chiqish")
        choice = input("Tanlovni kiriting (1-5): ")

        if choice == "1":
            books = add_book(books)
            save_books(filename, books)
        elif choice == "2":
            books = update_book(books)
            save_books(filename, books)
        elif choice == "3":
            books = delete_book(books)
            save_books(filename, books)
        elif choice == "4":
            list_books(books)
        elif choice == "5":
            print("Dastur yakunlandi. Xayr!")
            break
        else:
            print("❌ Noto'g'ri tanlov, iltimos 1 dan 5 gacha tanlang.")

if __name__ == "__main__":
    main()



# 4)Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.
# Vazifa: Filmni tavsiya qilish tizimi
# Filmlar haqida ma'lumot olish uchun http://www.omdbapi.com/ ushbu urldan foydalaning.
# Foydalanuvchilardan kino janrini so'raydigan va shu janrdan tasodifiy filmni tavsiya qiladigan dastur yarating.

import requests
import random

# OMDb API kalitini shu yerga yozing (yoki thewdb demo kalitdan foydalaning)
API_KEY = "thewdb"  # O'zingizning API kalitingiz bo'lsa, shuni yozing

def get_movie_by_genre(genre):
    # OMDb API to'g'ridan-to'g'ri genre asosida random kino bermaydi
    # Shuning uchun "search" parametrlari bilan ishlaymiz (demo cheklangan)
    # Ko'p mashhur so'zlardan foydalanamiz, janrga moslashtiramiz

    search_terms = ["love", "war", "future", "life", "death", "game", "dark", "man", "girl", "day"]
    random.shuffle(search_terms)

    for term in search_terms:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={term}&type=movie"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            movies = data.get("Search", [])
            random.shuffle(movies)

            for movie in movies:
                movie_id = movie['imdbID']
                movie_details_url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={movie_id}"
                details_response = requests.get(movie_details_url)
                details = details_response.json()

                if genre.lower() in details.get("Genre", "").lower():
                    return details

    return None

# Foydalanuvchidan janrni so'rash
genre_input = input("Qanday janrdagi film tavsiya qilaylik? (Masalan: Action, Comedy, Drama, Sci-Fi): ")

recommended = get_movie_by_genre(genre_input)

if recommended:
    print("\n🎬 Siz uchun tavsiya qilinadigan film:\n")
    print(f"🎞️ Nomi      : {recommended['Title']}")
    print(f"📆 Yili      : {recommended['Year']}")
    print(f"🎭 Janri     : {recommended['Genre']}")
    print(f"📝 Tavsifi   : {recommended['Plot']}")
    print(f"⭐ IMDB Reyting: {recommended['imdbRating']}")
    print(f"🔗 IMDB Link : https://www.imdb.com/title/{recommended['imdbID']}")
else:
    print("❌ Uzr, bu janr uchun film topilmadi. Boshqa janr sinab ko'ring.")


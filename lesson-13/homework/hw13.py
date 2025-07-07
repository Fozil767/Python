# 1)Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
# Yosh kalkulyatori: foydalanuvchidan tug'ilgan sanasini kiritishni so'rang. Ularning yoshini yillar, oylar va kunlarda hisoblang va chop eting.

from datetime import datetime

# 1. Foydalanuvchidan tug‘ilgan sanani kiritishini so‘raymiz
tugilgan_sana_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD formatda): ")

# 2. Kiritilgan sanani datetime formatiga o‘tkazamiz
tugilgan_sana = datetime.strptime(tugilgan_sana_str, "%Y-%m-%d")

# 3. Bugungi sanani olamiz
bugun = datetime.today()

# 4. Farqni hisoblaymiz
yil_farqi = bugun.year - tugilgan_sana.year
oy_farqi = bugun.month - tugilgan_sana.month
kun_farqi = bugun.day - tugilgan_sana.day

# 5. Agar kun yoki oy manfiy bo‘lsa, to‘g‘rilaymiz
if kun_farqi < 0:
    oy_farqi -= 1
    kun_farqi += (datetime(bugun.year, bugun.month, 1) - datetime(bugun.year, bugun.month - 1, 1)).days

if oy_farqi < 0:
    yil_farqi -= 1
    oy_farqi += 12

# 6. Natijani chiqaramiz
print(f"Sizning yoshingiz: {yil_farqi} yil, {oy_farqi} oy, {kun_farqi} kun.")

# 2)Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
# Keyingi tug'ilgan kungacha bo'lgan kunlar: Birinchi mashqga o'xshash, ammo bu safar foydalanuvchining keyingi tug'ilgan kuniga qadar qolgan kunlar sonini hisoblang va chop eting.

from datetime import datetime, timedelta

# 1. Foydalanuvchidan tug‘ilgan sanani olamiz (faqat oy va kun kerak)
tugilgan_sana_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD formatda): ")
tugilgan_sana = datetime.strptime(tugilgan_sana_str, "%Y-%m-%d")

# 2. Bugungi sanani olamiz
bugun = datetime.today()

# 3. Keyingi tug‘ilgan kunni aniqlaymiz
keyingi_tugilgan_kun = tugilgan_sana.replace(year=bugun.year)

# Agar tug‘ilgan kun bu yil allaqachon o‘tgan bo‘lsa, keyingi yilga o‘tkazamiz
if keyingi_tugilgan_kun < bugun:
    keyingi_tugilgan_kun = keyingi_tugilgan_kun.replace(year=bugun.year + 1)

# 4. Farqni (kunlar sonini) hisoblaymiz
kunlar_qoldi = (keyingi_tugilgan_kun - bugun).days

# 5. Natijani chiqaramiz
print(f"Sizning keyingi tug‘ilgan kuningizgacha {kunlar_qoldi} kun qoldi.")

# 3)Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
# Uchrashuvni rejalashtiruvchi: foydalanuvchidan joriy sana va vaqtni, shuningdek, uchrashuv davomiyligini soat va daqiqalarda kiritishni so'rang. Uchrashuv tugash sanasi va vaqtini hisoblang va chop eting.

from datetime import datetime, timedelta

# 1. Hozirgi sana va vaqtni foydalanuvchidan olamiz
hozir_str = input("Hozirgi sana-vaqtni kiriting (YYYY-MM-DD HH:MM formatda): ")
hozir = datetime.strptime(hozir_str, "%Y-%m-%d %H:%M")

# 2. Uchrashuv davomiyligini olamiz
soat = int(input("Uchrashuv davomiyligini soatlarda kiriting: "))
daqiqa = int(input("Uchrashuv davomiyligini daqiqalarda kiriting: "))

# 3. Uchrashuv davomiyligini timedelta shaklida yaratamiz
davomiylik = timedelta(hours=soat, minutes=daqiqa)

# 4. Tugash vaqtini hisoblaymiz
tugash_vaqti = hozir + davomiylik

# 5. Natijani chiqaramiz
print("Uchrashuv tugash vaqti:", tugash_vaqti.strftime("%Y-%m-%d %H:%M"))


# 4)Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

import pytz

from datetime import datetime
import pytz

# Foydalanuvchidan ma'lumotlarni olish
sana_vaqt_str = input("Sana-vaqtni kiriting (YYYY-MM-DD HH:MM formatda): ")
manba_timezone = input("Hozirgi vaqt zonangizni kiriting (masalan: Asia/Tashkent): ")
maqsad_timezone = input("Qaysi vaqt zonasiga o‘girishni xohlaysiz? (masalan: US/Eastern): ")

# Sana va vaqtni datetime obyektiga aylantirish
sana_vaqt = datetime.strptime(sana_vaqt_str, "%Y-%m-%d %H:%M")

# Vaqt zonalarini olish
try:
    manba_tz = pytz.timezone(manba_timezone)
    maqsad_tz = pytz.timezone(maqsad_timezone)
except pytz.UnknownTimeZoneError:
    print("Kiritilgan vaqt zonasi noto‘g‘ri. Iltimos, to‘g‘ri zonani kiriting.")
    exit()

# Lokal vaqtni manba zonasiga bog‘lash
local_dt = manba_tz.localize(sana_vaqt)

# Maqsad vaqt zonasiga aylantirish
converted_dt = local_dt.astimezone(maqsad_tz)

# Natijani chiqarish
print(f"\n{sana_vaqt_str} ({manba_timezone}) => {converted_dt.strftime('%Y-%m-%d %H:%M')} ({maqsad_timezone})")



# 5)Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
# Ortga hisoblash taymeri: Orqaga hisoblash taymerini qo'llang. Foydalanuvchidan kelajakdagi sana va vaqtni kiritishni so'rang, so'ngra ushbu nuqtaga qadar qolgan vaqtni muntazam ravishda (masalan, har soniyada) chop etishni so'rang.

import time
from datetime import datetime

# Foydalanuvchidan kelajakdagi sana va vaqtni so'raymiz
future_input = input("Kelajakdagi vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")

try:
    # Stringni datetime formatga aylantiramiz
    future_time = datetime.strptime(future_input, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        remaining = future_time - now

        if remaining.total_seconds() <= 0:
            print("⏰ Vaqt tugadi!")
            break

        # Kun, soat, daqiqa, soniyaga ajratib chiqaramiz
        days = remaining.days
        hours, rem = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        print(f"⏳ Qolgan vaqt: {days} kun, {hours} soat, {minutes} daqiqa, {seconds} soniya", end="\r")

        time.sleep(1)  # Har 1 soniyada yangilanadi

except ValueError:
    print("❌ Format noto'g'ri! Iltimos, 'YYYY-MM-DD HH:MM:SS' shaklida kiriting.")


# <!-- 6)Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format. -->
# Email Validator: Elektron pochta manzillarini tasdiqlovchi dasturni yozing. Foydalanuvchidan elektron pochta manzilini kiritishini so'rang va u to'g'ri elektron pochta formatiga mos kelishini tekshiring.


import re  # Regex kutubxonasi

# Email tekshiruvchi funksiyani aniqlaymiz
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Foydalanuvchidan emailni so‘raymiz
email_input = input("Email manzilingizni kiriting: ")

# Tekshiruv
if is_valid_email(email_input):
    print("✅ Email manzili to'g'ri formatda!")
else:
    print("❌ Noto'g'ri email formati. Iltimos, qaytadan tekshirib kiriting.")
# 7)Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
#Telefon raqamini formatlovchi: telefon raqamini kiritish sifatida qabul qiladigan va uni standart formatga muvofiq formatlaydigan dastur yarating. Masalan, "1234567890" ni "(123) 456-7890" ga aylantiring.

def format_phone_number(phone):
    # Faqat raqamlarni ajratib olamiz
    digits = ''.join(filter(str.isdigit, phone))

    # Raqamlar soni 10 ta bo‘lishi kerak
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return formatted
    else:
        return "❌ Noto'g'ri raqam formati. 10 ta raqam bo'lishi kerak."

# Foydalanuvchidan telefon raqamini so‘raymiz
user_input = input("Telefon raqamingizni kiriting (faqat raqamlar yoki istalgan formatda): ")
print("📞 Formatlangan:", format_phone_number(user_input))


#8) Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
# Parol kuchini tekshirgich: Parol kuchini tekshirgichni amalga oshiring. Foydalanuvchidan parolni kiritishini so'rang va uning ma'lum mezonlarga javob berishini tekshiring (masalan, minimal uzunlik, kamida bitta katta harf, bitta kichik harf va bitta raqamdan iborat).

import re

def check_password_strength(password):
    errors = []

    if len(password) < 8:
        errors.append("🔸 Parol kamida 8 ta belgidan iborat bo'lishi kerak.")
    if not re.search(r'[A-Z]', password):
        errors.append("🔸 Parolda kamida 1 ta katta harf bo'lishi kerak.")
    if not re.search(r'[a-z]', password):
        errors.append("🔸 Parolda kamida 1 ta kichik harf bo'lishi kerak.")
    if not re.search(r'[0-9]', password):
        errors.append("🔸 Parolda kamida 1 ta raqam bo'lishi kerak.")

    if errors:
        print("❌ Parol kuchsiz:")
        for error in errors:
            print(error)
    else:
        print("✅ Parol kuchli!")

# Foydalanuvchidan parol olish
user_password = input("🔐 Parol kiriting: ")
check_password_strength(user_password)

#9) Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
#Word Finder: Berilgan matnda ma'lum bir so'zning barcha ko'rinishlarini topadigan dastur ishlab chiqing. Foydalanuvchidan so'z kiritishni so'rang, so'ngra namuna matnida ushbu so'zning barcha uchraydigan joylarini qidiring va chop eting.

def find_word_occurrences(text, word):
    word = word.lower()
    text_lower = text.lower()
    index = 0
    positions = []

    while index < len(text_lower):
        index = text_lower.find(word, index)
        if index == -1:
            break
        positions.append(index)
        index += len(word)

    return positions

# Foydalanuvchidan matn va qidiriladigan so'z olish
sample_text = input("📄 Matn kiriting: ")
search_word = input("🔍 Qidirilayotgan so'zni kiriting: ")

# Qidiruv
positions = find_word_occurrences(sample_text, search_word)

# Natija chiqarish
if positions:
    print(f"✅ So'z '{search_word}' {len(positions)} marta topildi.")
    print(f"📌 Joylashuv indekslari: {positions}")
else:
    print(f"❌ So'z '{search_word}' topilmadi.")

#10) Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
#Sana Extractor: Berilgan matndan sanalarni ajratib oluvchi dastur tuzing. Foydalanuvchidan matn kiritishni so'rang, so'ngra matndagi barcha sanalarni aniqlang va chop eting.

import re

# Sana uchun patternlar (regex)
date_patterns = [
    r'\b\d{2}/\d{2}/\d{4}\b',   # 01/01/2025
    r'\b\d{2}-\d{2}-\d{4}\b',   # 01-01-2025
    r'\b\d{4}-\d{2}-\d{2}\b',   # 2025-01-01
    r'\b\d{2}\.\d{2}\.\d{4}\b', # 01.01.2025
    r'\b\w+ \d{1,2}, \d{4}\b',  # January 1, 2025
]

# Matn olish
text = input("📝 Matn kiriting (sana bo'lgan):\n")

# Topilgan sanalar ro'yxati
found_dates = []

# Har bir pattern bo‘yicha sanalarni topish
for pattern in date_patterns:
    found_dates.extend(re.findall(pattern, text))

# Natijani chiqarish
if found_dates:
    print("\n📅 Topilgan sanalar:")
    for date in found_dates:
        print(f"➤ {date}")
else:
    print("\n🚫 Sana topilmadi.")



#1)def is_leap(year): """ Determines whether a given year is a leap year.def is_leap(year): """ Berilgan yil kabisa yili ekanligini aniqlaydi.

def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2020))  # ✅ True (kabisa yili)
print(is_leap(1900))  # ❌ False (100 ga bo‘linadi, 400 ga emas)
print(is_leap(2000))  # ✅ True (400 ga bo‘linadi)

#2)Given an integer, n, perform the following conditional actions:
def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

# Misol uchun chaqiramiz:
n = int(input("Butun son kiriting: "))
check_weird(n)

#3)Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
#A va b ikkita butun son berilgan. Bu raqamlar orasidagi juft sonlarni toping. a va b o'z ichiga oladi. Loop ishlatmang.

a = 3
b = 12

# if-else bilan chegaralarni to‘g‘rilash
start = a if a % 2 == 0 else a + 1  # juftlikka to‘g‘rilash
end = b if b % 2 == 0 else b - 1

even_numbers = list(range(start, end + 1, 2))
print("Juft sonlar (if-else bilan):", even_numbers)

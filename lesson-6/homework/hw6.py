def insert_underscore(txt):
    vowels = 'aeiouAEIOU'
    result = ''
    i = 0
    count = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        # Har uchinchi belgidan so'ng underscore qo'shish
        if count == 3:
            # Keyingi belgini tekshirish uchun mavjudligini tekshiramiz
            if (txt[i] in vowels) or (i + 1 < len(txt) and txt[i + 1] == '_'):
                pass  # Underscore ni hozircha qo‘shmaymiz
            elif i + 1 < len(txt):  # So‘ngida underscore qo‘shilmasligi uchun
                result += '_'
            count = 0  # Sanashni qayta boshlaymiz
        i += 1

    return result
print(insert_underscore("abcdefghijk"))    #3.3 Calculate sum of all numbers from 1 to a given number.1 dan berilgan songacha bo'lgan barcha sonlar yig'indisini hisoblang

n = int(input("Enter number: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum is:", total)


# ➤ "abc_def_ghi_jk"

print(insert_underscore("aeioubcdfg"))    
# ➤ "aeioub_cdf_g"

print(insert_underscore("a1e2i3o4u5b6c7")) 
# ➤ "a1e2i3o4u5b_6c_7"

#2)The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
#Taqdim etilgan kod stubkasi STDIN dan butun sonni, n ni o'qiydi. 0 <= i < n bo'lgan barcha manfiy bo'lmagan butun sonlar uchun i^2 ni chop eting.

n = int(input("n ni kiriting: "))

for i in range(n):
    print(i ** 2)


#3)Exercise 1: Print first 10 natural numbers using a while loop
#Exercise 2: Print the following pattern. 1-mashq: Birinchi 10 natural sonni while siklidan foydalanib chop eting
#2-mashq: Quyidagi naqshni chop eting

i = 1
while i <= 10:
    print(i)
    i += 1

#----2 mashq
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print(col, end=" ")
        col += 1
    print()  # yangi qatordan yozish
    row += 1


#Exercise 4: Print multiplication table of a given number. Berilgan sonni ko‘paytirish jadvalini chop eting

num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(num * i)
    i += 1

#Exercise 5: Display numbers from a list using a loop. Loop yordamida ro'yxatdagi raqamlarni ko'rsatish

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    print(num)

#Exercise 6: Count the total number of digits in a number. sondagi raqamlarning umumiy sonini hisoblang
num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10
    count += 1

print("Total digits:", count)
#Exercise 7: Print reverse number pattern. Teskari raqam naqshini chop eting
row = 5
while row >= 1:
    col = row
    while col >= 1:
        print(col, end=" ")
        col -= 1
    print()  # yangi qator
    row -= 1



#Exercise 8: Print list in reverse order using a loop. Loop yordamida ro'yxatni teskari tartibda chop eting

list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
  #Exercise 9: Display numbers from -10 to -1 using a for loop. For tsikli yordamida -10 dan -1 gacha raqamlarni ko'rsatish

for i in range(-10, 0):
    print(i)


#Exercise 10: Display message “Done” after successful loop execution. Muvaffaqiyatli tsikl bajarilgandan so'ng "Bajarildi" xabarini ko'rsatish
for i in range(5):
    print(i)
else:
    print("Done!")


#Exercise 11: Print all prime numbers within a range. diapazondagi barcha tub sonlarni chop eting

for num in range(25, 51):
    if num > 1:  # 1 tub son emas
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


#Exercise 12: Display Fibonacci series up to 10 terms.12-mashq: Fibonachchi seriyasini 10 tagacha ko'rsating

# 10 ta Fibonacci sonini chiqarish
n = 10
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#Exercise 13: Find the factorial of a given number. 13-mashq: Berilgan sonning faktorialini toping
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Faktorial manfiy sonlar uchun aniqlanmagan.")
elif num == 0:
    print("0! = 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"{num}! = {factorial}")

#14)Return the elements that are not common between two lists. The order of elements does not matter.
#Ikki ro'yxat o'rtasida umumiy bo'lmagan elementlarni qaytaring. Elementlarning tartibi muhim emas

from collections import Counter

def not_common_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    diff = (c1 - c2) + (c2 - c1)
    result = list(diff.elements())
    
    return result

print(not_common_elements([1, 1, 2], [2, 3, 4]))      
# ➞ [1, 1, 3, 4]

print(not_common_elements([1, 2, 3], [4, 5, 6]))      
# ➞ [1, 2, 3, 4, 5, 6]

print(not_common_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
# ➞ [2, 2, 5]


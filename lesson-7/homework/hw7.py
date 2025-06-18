#1. is_prime(n) funksiyasi
#is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(4))   # ➞ False
print(is_prime(7))   # ➞ True
print(is_prime(1))   # ➞ False
print(is_prime(2))   # ➞ True
print(is_prime(9))   # ➞ False

#2. digit_sum(k) funksiyasi digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

print(digit_sum(24))   # ➞ 6   (2 + 4)
print(digit_sum(502))  # ➞ 7   (5 + 0 + 2)
print(digit_sum(1001)) # ➞ 2   (1 + 0 + 0 + 1)

#3. Ikki sonning darajalari
#Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def print_powers_of_two(N):
    power = 1
    while power * 2 <= N:
        power *= 2
        print(power, end=' ')

print_powers_of_two(10)
# ➞ 2 4 8

print()  # yangi qatordan chiqarish

print_powers_of_two(20)
# ➞ 2 4 8 16

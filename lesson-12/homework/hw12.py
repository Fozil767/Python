import threading

# Tub sonni aniqlovchi funksiya
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Har bir thread uchun ishlovchi funksiya
def check_primes_in_range(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

# Asosiy kod
if __name__ == "__main__":
    start_range = 1
    end_range = 100
    thread_count = 4

    # Har bir thread ga bo‘linadigan oraliqni aniqlash
    step = (end_range - start_range) // thread_count
    threads = []
    results = [[] for _ in range(thread_count)]  # Har bir thread uchun alohida natijalar

    # Threadlarni yaratish va ishga tushurish
    for i in range(thread_count):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i < thread_count - 1 else end_range
        t = threading.Thread(target=check_primes_in_range, args=(start, end, results[i]))
        threads.append(t)
        t.start()

    # Barcha threadlar tugaguncha kutish
    for t in threads:
        t.join()

    # Natijalarni birlashtirish va chiqarish
    all_primes = []
    for prime_list in results:
        all_primes.extend(prime_list)

    all_primes.sort()
    print("Prime numbers in range:", all_primes)

import threading
from collections import defaultdict

# Har bir thread uchun ishlovchi funksiya
def count_words(lines, result_dict, lock):
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            local_count[word] += 1

    # Natijalarni umumiy lug‘atga qo‘shish (lock bilan)
    with lock:
        for word, count in local_count.items():
            result_dict[word] += count

# Asosiy kod
def main():
    filename = "sample_text.txt"
    thread_count = 4
    result_dict = defaultdict(int)
    lock = threading.Lock()

    # Fayldan barcha qatorlarni o‘qish
    with open(filename, "r") as file:
        lines = file.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // thread_count
    threads = []

    for i in range(thread_count):
        start_index = i * chunk_size
        # Oxirgi thread qolgan barcha qatordan foydalanadi
        end_index = (i + 1) * chunk_size if i != thread_count - 1 else total_lines
        thread_lines = lines[start_index:end_index]

        t = threading.Thread(target=count_words, args=(thread_lines, result_dict, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Natijalarni chiqarish
    print("\n📊 Word Frequency Summary:")
    for word, count in sorted(result_dict.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()

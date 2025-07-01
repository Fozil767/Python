#1. Circle Class
#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
#Circleni ifodalovchi sinf yaratish uchun Python dasturini yozing. Uning maydoni va perimetrini hisoblash usullarini kiriting

import math  # pi soni uchun math kutubxonasini chaqiramiz

# Aylana klassini yaratamiz
class Circle:
    def __init__(self, radius):  # radius – aylananing radiusi
        self.radius = radius      # obyektning radius xususiyatiga qiymat beramiz

    def area(self):  # Yuzani hisoblaydigan metod
        return math.pi * self.radius ** 2

    def perimeter(self):  # Perimetrni hisoblaydigan metod
        return 2 * math.pi * self.radius

# >>> Foydalanuvchidan radiusni so‘raymiz:
r = float(input("Aylananing radiusini kiriting: "))

# Circle klassidan obyekt yaratamiz
c = Circle(r)

# Natijalarni chiqaramiz
print(f"Aylananing yuzi: {c.area():.2f}")
print(f"Aylananing perimetri: {c.perimeter():.2f}")

#2)Person Class
#Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.
#Person sinfini yaratish uchun Python dasturini yozing. Ism, mamlakat va tug'ilgan sana kabi atributlarni qo'shing. Shaxsning yoshini aniqlash usulini qo'llang


from datetime import datetime

# Person klassi
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        # Agar tug‘ilgan sana hali bu yil kelmagan bo‘lsa, yoshdan 1 ayiramiz
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

# >>> Foydalanuvchidan ma'lumot so‘raymiz
name = input("Ismingizni kiriting: ")
country = input("Davlatingizni kiriting: ")
dob = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")

# Person obyektini yaratamiz
person = Person(name, country, dob)

# Natija
print(f"{person.name} ({person.country}) hozirda {person.calculate_age()} yoshda.")


#3)Calculator Class
#Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
#Kalkulyator sinfini yaratish uchun Python dasturini yozing. Asosiy arifmetik amallar uchun usullarni kiriting.

# Calculator klassi
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Xatolik: 0 ga bo‘lish mumkin emas!"
        return x / y

# Calculator obyektini yaratamiz
calc = Calculator()

# Foydalanuvchi inputi
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

# Har bir amalni alohida ko‘rsatamiz
print("Qo‘shish:", calc.add(a, b))
print("Ayirish:", calc.subtract(a, b))
print("Ko‘paytirish:", calc.multiply(a, b))
print("Bo‘lish:", calc.divide(a, b))

#4)Shape and Subclasses
#Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
#Shaklni ifodalovchi sinf yaratish uchun Python dasturini yozing. Uning maydoni va perimetrini hisoblash usullarini kiriting. Doira, Uchburchak va Kvadrat kabi turli shakllar uchun kichik sinflarni amalga oshiring.

import math

# Asosiy klass (Shape)
class Shape:
    def area(self):
        pass  # Bo‘sh, subklasslar to‘ldiradi

    def perimeter(self):
        pass

# Aylana (Circle) klassi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Kvadrat (Square) klassi
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Uchburchak (Triangle) klassi
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# ========== Sinov ==========
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Aylana yuzasi:", round(circle.area(), 2))
print("Aylana perimetri:", round(circle.perimeter(), 2))

print("Kvadrat yuzasi:", square.area())
print("Kvadrat perimetri:", square.perimeter())

print("Uchburchak yuzasi:", round(triangle.area(), 2))
print("Uchburchak perimetri:", triangle.perimeter())



#5 Binary Search Tree Class
#Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
#Ikkilik qidiruv daraxtini ifodalovchi sinf yaratish uchun Python dasturini yozing. Ikkilik daraxtga elementlarni kiritish va qidirish usullarini qo'shing.

# Har bir tugun uchun Node klassi
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # Chap farzand
        self.right = None  # O‘ng farzand

# BST daraxt klassi
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Daraxtning boshlanishi

    # Element qo‘shish metodi
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        else:
            print(f"{value} daraxtda mavjud.")

    # Elementni izlash metodi
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

# ==== Sinov uchun ====
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Izlash
print("40 mavjudmi?", bst.search(40))  # True
print("25 mavjudmi?", bst.search(25))  # False



#6)Stack Data Structure
#Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
#Stack ma'lumotlar strukturasini ifodalovchi sinf yaratish uchun Python dasturini yozing. Elementlarni surish va ochish usullarini qo'shing.

class Stack:
    def __init__(self):
        self.items = []  # Bo‘sh ro‘yxat bilan boshlanadi

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"{item} stekga qo‘shildi.")

    def pop(self):
        if self.is_empty():
            print("Stek bo‘sh! Element yo‘q.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stek bo‘sh.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stekdagi elementlar:", self.items)

# === Sinov uchun ===
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Pop:", s.pop())  # 30 ni olib tashlaydi
s.display()

print("Stek o‘lchami:", s.size())
print("Yuqoridagi element:", s.peek())


#7)Linked List Data Structure
#Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
#Bog'langan ro'yxat ma'lumotlar strukturasini ifodalovchi sinf yaratish uchun Python dasturini yozing. Bog'langan ro'yxat ma'lumotlarini ko'rsatish, tugunlarni kiritish va o'chirish usullarini qo'shing.

# Tugun klassi (har bir element uchun)
class Node:
    def __init__(self, data):
        self.data = data        # Tugunning qiymati
        self.next = None        # Keyingi tugunga havola

# LinkedList klassi
class LinkedList:
    def __init__(self):
        self.head = None        # Bosh tugun (ro‘yxat boshida yo‘q)

    # Linked listga element qo‘shish (oxiriga)
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:     # Oxirgi tugungacha yur
                current = current.next
            current.next = new_node
        print(f"{data} ro‘yxatga qo‘shildi.")

    # Tugunni chiqarish (display qilish)
    def display(self):
        current = self.head
        if current is None:
            print("Ro‘yxat bo‘sh.")
            return
        print("Linked list elementlari: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Elementni o‘chirish
    def delete(self, key):
        current = self.head
        prev = None

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} ro‘yxatda topilmadi.")
            return

        if prev is None:
            self.head = current.next  # Birinchi element bo‘lsa
        else:
            prev.next = current.next

        print(f"{key} ro‘yxatdan o‘chirildi.")

# === Sinov uchun ===
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()

ll.delete(50)  # Topilmaydi

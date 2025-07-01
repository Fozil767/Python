#1 Create your own virtual environment and install some python packages.
#O'zingizning virtual muhitingizni yarating va ba'zi python paketlarini o'rnating.

# Yangi papka yaratish (ixtiyoriy)
mkdir my_project
cd my_project

# Virtual environment yaratish
python -m venv venv

#2 Create custom modules.
#Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
#Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
#math_operations.py modulini yarating. Undagi qo‘shish, ayirish, ko‘paytirish va bo‘lish funksiyalarini aniqlang. (Bu vazifada barcha funksiyalar ikkita argumentni qabul qiladi)
#string_utils.py modulini yarating. Undagi teskari_string va count_vowels funksiyalarini aniqlang. (Bu vazifada barcha funksiyalar bitta argumentni qabul qiladi)

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
#Create custom packages.
#Create geometry package.
# geometry\
 #    __init__.py
  #   circle.py

# geometry/circle.py

import math

def area(radius):
    """Doiraning yuzasini hisoblaydi."""
    return math.pi * radius * radius

def perimeter(radius):
    """Doiraning uzunligini hisoblaydi (perimetri)."""
    return 2 * math.pi * radius


#Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
#Create file_operations package.
# file_operations\
#     __init__.py
 #    file_reader.py
  #   file_writer.py
# geometry/circle.py

import math

def calculate_area(radius):
    """Doiraning yuzasini hisoblash"""
    return math.pi * radius * radius

def calculate_circumference(radius):
    """Doiraning perimetrini hisoblash"""
    return 2 * math.pi * radius

#1)Define Task Class:
#Create a Task class with attributes such as task title, description, due date, and status.
#Vazifa nomi, tavsifi, tugash sanasi va holati kabi atributlarga ega Vazifa sinfini yarating

# Task klassi
class Task:
    def __init__(self, title, description, due_date, status="bajarilmagan"):
        self.title = title                  # Vazifa nomi
        self.description = description      # Vazifa tavsifi
        self.due_date = due_date            # Tugash sanasi
        self.status = status                # Holat (default: bajarilmagan)

    # Vazifa haqida ma'lumot chiqarish
    def display_task(self):
        print("🔹 Vazifa nomi:", self.title)
        print("📝 Tavsifi:", self.description)
        print("📅 Tugash sanasi:", self.due_date)
        print("✅ Holat:", self.status)

    # Holatni o'zgartirish
    def mark_as_done(self):
        self.status = "bajarildi"
        print(f"✅ '{self.title}' vazifasi bajarildi deb belgilandi.")

# === Sinov ===
task1 = Task("Python o'rganish", "OOP bo'yicha mashq bajarish", "2025-06-15")
task1.display_task()

print("\n--- Holat o‘zgartirilmoqda ---")
task1.mark_as_done()
task1.display_task()

#2)Define ToDoList Class:
#Create a ToDoList class that manages a list of tasks.
#Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
#Vazifalar ro'yxatini boshqaradigan ToDoList sinfini yarating.
#Vazifa qo'shish, vazifani tugallangan deb belgilash, barcha vazifalarni sanab o'tish va tugallanmagan vazifalarni ko'rsatish usullarini qo'shing.

# Task klassi – bitta vazifani ifodalaydi
class Task:
    def __init__(self, title, description, due_date, status="bajarilmagan"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_as_done(self):
        self.status = "bajarildi"

    def display(self):
        print(f"🔸 Nomi: {self.title}")
        print(f"📄 Tavsifi: {self.description}")
        print(f"📅 Tugash sanasi: {self.due_date}")
        print(f"✅ Holat: {self.status}")
        print("-" * 30)


# ToDoList klassi – bir nechta vazifalarni boshqaradi
class ToDoList:
    def __init__(self):
        self.tasks = []

    # Vazifa qo‘shish
    def add_task(self, task):
        self.tasks.append(task)
        print(f"➕ Yangi vazifa qo‘shildi: {task.title}")

    # Vazifani bajarildi deb belgilash
    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_done()
                print(f"✅ '{title}' bajarildi deb belgilandi.")
                return
        print(f"⚠️ Vazifa topilmadi: {title}")

    # Barcha vazifalarni chiqarish
    def list_all_tasks(self):
        if not self.tasks:
            print("📭 Vazifalar yo‘q.")
        else:
            print("📋 Barcha vazifalar:")
            for task in self.tasks:
                task.display()

    # Bajarilmagan vazifalarni chiqarish
    def display_incomplete_tasks(self):
        print("⏳ Bajarilmagan vazifalar:")
        for task in self.tasks:
            if task.status == "bajarilmagan":
                task.display()


# ==== Test qilish ====
todo = ToDoList()

# Vazifalar yaratish
task1 = Task("Python o‘rganish", "Klass va obyektlar", "2025-06-15")
task2 = Task("Excel mashq qilish", "Pivot table", "2025-06-16")
task3 = Task("SQL yozish", "Window function", "2025-06-17")

# Qo‘shish
todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

print("\n--- Barcha vazifalar ---")
todo.list_all_tasks()

print("\n--- Bajarilmaganlar ---")
todo.display_incomplete_tasks()

print("\n--- Bittasini bajarildi deb belgilash ---")
todo.mark_task_complete("Excel mashq qilish")

print("\n--- Yana bajarilmaganlarni ko‘rish ---")
todo.display_incomplete_tasks()

#3)Create Main Program:
#Develop a CLI to interact with the Blog system.
#Include options to add posts, list all posts, and display posts by a specific author.
#Blog tizimi bilan ishlash uchun CLI ni ishlab chiqing.
#Xabarlar qo'shish, barcha xabarlarni ro'yxatga olish va ma'lum bir muallifning xabarlarini ko'rsatish uchun variantlarni qo'shing.

# Post klassi – bitta postni ifodalaydi
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"📌 Sarlavha: {self.title}")
        print(f"✍️ Muallif: {self.author}")
        print(f"📄 Post: {self.content}")
        print("-" * 30)

# Blog klassi – bir nechta postlarni boshqaradi
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("✅ Post muvaffaqiyatli qo‘shildi.\n")

    def list_all_posts(self):
        if not self.posts:
            print("📭 Postlar yo‘q.\n")
        else:
            print("🗃 Barcha postlar:")
            for post in self.posts:
                post.display()

    def display_by_author(self, author_name):
        found = False
        print(f"✍️ Muallif: {author_name} postlari:")
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                post.display()
                found = True
        if not found:
            print("⚠️ Ushbu muallifda hech qanday post yo‘q.\n")

#4)Enhance Blog System:
#Add functionality to delete a post, edit a post, and display the latest posts.
#Blog tizimini takomillashtirish:
#Xabarni oʻchirish, postni tahrirlash va soʻnggi xabarlarni koʻrsatish uchun funksiya qoʻshing.

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("✅ Post muvaffaqiyatli qo‘shildi.\n")

    def list_all_posts(self):
        if not self.posts:
            print("📭 Postlar yo‘q.\n")
        else:
            print("🗃 Barcha postlar:")
            for idx, post in enumerate(self.posts, 1):
                print(f"ID: {idx}")
                post.display()

    def display_by_author(self, author_name):
        found = False
        print(f"✍️ Muallif: {author_name} postlari:")
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                post.display()
                found = True
        if not found:
            print("⚠️ Ushbu muallifda hech qanday post yo‘q.\n")

    def delete_post(self, post_id):
        if 1 <= post_id <= len(self.posts):
            removed_post = self.posts.pop(post_id - 1)
            print(f"🗑 Post o‘chirildi: {removed_post.title}\n")
        else:
            print("❌ Noto‘g‘ri post ID.\n")

    def edit_post(self, post_id, new_title=None, new_content=None):
        if 1 <= post_id <= len(self.posts):
            post = self.posts[post_id - 1]
            if new_title:
                post.title = new_title
            if new_content:
                post.content = new_content
            print("✏️ Post muvaffaqiyatli tahrirlandi.\n")
        else:
            print("❌ Noto‘g‘ri post ID.\n")

    def display_latest_posts(self, count=3):
        print(f"🆕 So‘nggi {count} ta post:")
        for post in self.posts[-count:]:
            post.display()


#5)Test the Application:
#Create instances of posts and test the functionality of your Blog system.
#Xabar namunalarini yarating va Blog tizimingiz funksionalligini sinab ko'ring.

# Post va Blog klasslarini import qiling (yoki bir faylda yozilgan bo‘lsa, to‘g‘ridan-to‘g‘ri ishlating)

# Blog tizimi obyektini yaratamiz
my_blog = Blog()

# Test postlarini qo‘shamiz
post1 = Post("Python Darslari", "Bugun Python o‘rganamiz.", "Ali")
post2 = Post("Django Tutorial", "Web framework haqida.", "Vali")
post3 = Post("SQL Asoslari", "Ma'lumotlar bazasi bilan ishlash.", "Ali")
post4 = Post("Pandas Library", "Data analysis uchun kutubxona.", "Guli")

# Blogga postlarni qo‘shish
my_blog.add_post(post1)
my_blog.add_post(post2)
my_blog.add_post(post3)
my_blog.add_post(post4)

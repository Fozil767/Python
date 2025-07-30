import pandas as pd

# CSV faylni o‘qish va sanani datetime formatga o‘tkazish
df = pd.read_csv('task\\stackoverflow_qa.csv', parse_dates=['creationdate'])

# 1. 2014-yildan oldin yaratilgan savollar
before_2014 = df[df['creationdate'] < '2014-01-01']
print("📌 1. 2014-yildan oldin yaratilgan savollar:")
print(before_2014, "\n")

# 2. Score > 50 bo‘lgan savollar
score_above_50 = df[df['score'] > 50]
print("📌 2. Score > 50 bo‘lgan savollar:")
print(score_above_50, "\n")

# 3. Score 50 < x < 100 bo‘lgan savollar
score_between_50_100 = df[(df['score'] > 50) & (df['score'] < 100)]
print("📌 3. Score 50-100 oralig‘idagi savollar:")
print(score_between_50_100, "\n")

# 4. Scott Boston tomonidan javob berilgan savollar
answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print("📌 4. Scott Boston javob bergan savollar:")
print(answered_by_scott, "\n")

# 5. 5 ta foydalanuvchi tomonidan javob berilgan savollar
users = ['Scott Boston', 'unutbu', 'jezrael', 'DSM', 'Warren Weckesser']
answered_by_5_users = df[df['ans_name'].isin(users)]
print("📌 5. 5 ta foydalanuvchi javob bergan savollar:")
print(answered_by_5_users, "\n")

# 6. Mart–Okt 2014 oralig‘ida unutbu javob bergan, score < 5
unutbu_low_score = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'unutbu') &
    (df['score'] < 5)
]
print("📌 6. 2014 mart-okt: Unutbu javob bergan, score < 5:")
print(unutbu_low_score, "\n")

# 7. score 5–10 yoki viewcount > 10,000 bo‘lgan savollar


import pandas as pd

# CSV faylni o‘qish
titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Class 1dagi, yoshi 20–30 oralig‘ida bo‘lgan ayollar
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]
print("1. Class 1dagi, yoshi 20–30 oralig‘idagi ayollar:\n", female_class1_20_30, "\n")

# 2. Narxi $100 dan ko‘p bo‘lgan yo‘lovchilar
fare_above_100 = titanic_df[titanic_df['Fare'] > 100]
print("2. $100 dan ko‘p to‘lov qilgan yo‘lovchilar:\n", fare_above_100, "\n")

# 3. Yolg‘iz sayohat qilgan va omon qolganlar
survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print("3. Yolg‘iz bo‘lgan va omon qolgan yo‘lovchilar:\n", survived_alone, "\n")

# 4. C portidan chiqqan va $50 dan ko‘p to‘lov qilgan yo‘lovchilar
embarked_C_fare_50plus = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print("4. 'C' portidan chiqqan va $50+ to‘lagan yo‘lovchilar:\n", embarked_C_fare_50plus, "\n")

# 5. Ham SibSp, ham Parch mavjud bo‘lganlar
sibsp_and_parch = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
print("5. Ham qarindosh, ham farzand/ota-ona bilan chiqqanlar:\n", sibsp_and_parch, "\n")

# 6. 15 yoshdan kichik va omon qolmagan yo‘lovchilar
under15_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]
print("6. 15 yoshdan kichik va halok bo‘lgan yo‘lovchilar:\n", under15_not_survived, "\n")

# 7. Cabin bor va to‘lovi $200 dan katta bo‘lganlar
cabin_and_fare200plus = titanic_df[
    titanic_df['Cabin'].notnull() &
    (titanic_df['Fare'] > 200)
]
print("7. Cabin ko‘rsatilgan va $200+ to‘lov qilgan yo‘lovchilar:\n", cabin_and_fare200plus, "\n")

# 8. PassengerId toq son bo‘lgan yo‘lovchilar
odd_passenger_ids = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("8. Toq PassengerId ga ega bo‘lgan yo‘lovchilar:\n", odd_passenger_ids, "\n")

# 9. Faqat unikal (takrorlanmagan) Ticket raqamga ega yo‘lovchilar
unique_tickets = titanic_df[titanic_df.duplicated(subset='Ticket', keep=False) == False]
print("9. Unikal chipta raqamiga ega yo‘lovchilar:\n", unique_tickets, "\n")

# 10. 'Miss' so‘zi ismidan topilgan va Class 1da bo‘lgan ayollar
miss_in_name_class1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Name'].str.contains('Miss', case=False, na=False))
]
print("10. 'Miss' ismidan topilgan va Class 1da bo‘lgan ayollar:\n", miss_in_name_class1, "\n")

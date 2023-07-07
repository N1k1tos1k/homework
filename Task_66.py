"""
Создайте базу данных для хранения информации о студентах, включающую их имена,
возраст и средний балл. Затем выведите все данные на экран.
"""

# Подключаем библиотеку sqlite3
import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('database.db')

# Создаем курсор - специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# Создаем таблицу students
cursor.execute('''CREATE TABLE IF NOT EXISTS students
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, GPA INTEGER)''')

# Выполняем вставку записей в таблицу
cursor.execute("INSERT INTO students (name, age, GPA) VALUES (?, ?, ?)", ('John', 20, 4))
cursor.execute("INSERT INTO students (name, age, GPA) VALUES (?, ?, ?)", ('Helen', 21, 5))
cursor.execute("INSERT INTO students (name, age, GPA) VALUES (?, ?, ?)", ('Peter', 19, 3))

# Делаем выборку из таблицы
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()                   # Получение записей из выборки
for row in rows:                           # Построчный вывод записей на экран
    print(row)

# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()



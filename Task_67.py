Создайте базу данных для хранения информации о книгах, включающую их названия,
авторов и годы выпуска. Затем выведите все книги, выпущенные после 2000 года.
"""
# Подключаем библиотеку sqlite3
import sqlite3
from datetime import date  # Подключаем библиотеку datetime для работы с датой в таблице, т.к sqlite3 даты не поддерж.

# Подключаемся к базе данных
conn = sqlite3.connect('database_books.db', detect_types=sqlite3.PARSE_DECLTYPES)

# Создаем курсор - специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# Создаем таблицу books
cursor.execute('''CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY, name TEXT, author TEXT, release DATE)''')

# Выполняем вставку записей в таблицу
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Star Wars', 'Джордж Лукас', '1976-11-12'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Властелин Колец', 'Дж. Р. Р. Толкин', '1954-07-29'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Как разговаривать с кем угодно, когда угодно и где угодно', 'Кинг Л.', '2020-01-01'))

# Делаем выборку из таблицы
cursor.execute("SELECT * FROM books WHERE DATE(release) > '2000-01-01'")
rows = cursor.fetchall()                   # Получение записей из выборки
for row in rows:                           # Построчный вывод записей на экран
    print(row)

# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()


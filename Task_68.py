Создайте базу данных для хранения информации о фильмах, включающую их названия,
жанры и рейтинги. Затем выведите все фильмы выбранного жанра.
"""

# Подключаем библиотеку sqlite3
import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('database_films.db')

# Создаем курсор - специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# Создаем таблицу films
cursor.execute('''CREATE TABLE IF NOT EXISTS films
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating REAL)''')

# Выполняем вставку записей в таблицу
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Шина', 'Ужасы', 5.9))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Гарри Поттер', 'Приключения', 9))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Властелин Колец', 'Приключения', 8.9))

# Делаем выборку из таблицы
cursor.execute("SELECT * FROM films WHERE genre = 'Приключения'")
rows = cursor.fetchall()                   # Получение записей из выборки
for row in rows:                           # Построчный вывод записей на экран
    print(row)

# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()


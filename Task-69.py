Создайте базу данных для хранения информации о сотрудниках, включающую их имена,
должности и зарплаты. Затем выведите все имена сотрудников, занимающих должность
менеджера.
"""

# Подключаем библиотеку sqlite3
import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('database_employees.db')

# Создаем курсор - специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# Создаем таблицу employees
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
(id INTEGER PRIMARY KEY, name TEXT, function TEXT, salary REAL)''')

# Выполняем вставку записей в таблицу
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Петросян Никита Игоревич', 'Программист', 186500))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Артимов Александр Леонидович', 'Менеджер', 230000))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Кольцевой Анатолий Максимович', 'Уборщик', 30000))

# Делаем выборку из таблицы
cursor.execute("SELECT * FROM employees WHERE function = 'Менеджер'")
rows = cursor.fetchall()                   # Получение записей из выборки
for row in rows:                           # Построчный вывод записей на экран
    print(row)

# Фиксируем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()

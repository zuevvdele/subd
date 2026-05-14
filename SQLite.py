from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).resolve().parent / "db_00.sqlite"


# Задание 1. Создание базы данных, таблиц и связей
CREATE_TABLES_SQL = """
PRAGMA foreign_keys = OFF;

DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS gruppa;
DROP TABLE IF EXISTS specialty;

CREATE TABLE specialty (
    sp_code TEXT PRIMARY KEY,
    sp_name TEXT NOT NULL,
    qualification TEXT
);

CREATE TABLE gruppa (
    gr INTEGER PRIMARY KEY,
    sp_code TEXT NOT NULL,
    year_n INTEGER NOT NULL,
    FOREIGN KEY (sp_code) REFERENCES specialty(sp_code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fam TEXT NOT NULL,
    name TEXT NOT NULL,
    year_b INTEGER NOT NULL,
    gr INTEGER NOT NULL,
    FOREIGN KEY (gr) REFERENCES gruppa(gr)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

PRAGMA foreign_keys = ON;
"""


# Задание 2. Заполнение таблиц записями
INSERT_DATA_SQL = """
INSERT INTO specialty (sp_code, sp_name, qualification) VALUES
    ('09.02.07', 'Информационные системы и программирование', 'Программист'),
    ('09.02.06', 'Сетевое и системное администрирование', 'Администратор'),
    ('38.02.01', 'Экономика и бухгалтерский учет', 'Бухгалтер'),
    ('44.02.02', 'Преподавание в начальных классах', 'Учитель');

INSERT INTO gruppa (gr, sp_code, year_n) VALUES
    (1994, '09.02.07', 2024),
    (1995, '09.02.06', 2024),
    (1996, '38.02.01', 2023),
    (1997, '44.02.02', 2023);

INSERT INTO student (fam, name, year_b, gr) VALUES
    ('Иванов', 'Иван', 2004, 1994),
    ('Петрова', 'Анна', 2005, 1994),
    ('Сидоров', 'Петр', 2004, 1995),
    ('Смирнова', 'Ольга', 2006, 1996),
    ('Кузнецов', 'Максим', 2005, 1997);
"""


# Задание 3. Изменение года рождения студента с определенным id
UPDATE_STUDENT_SQL = """
UPDATE student
SET year_b = 2003
WHERE id = 1;
"""


# Задание 4. Удаление данных о студенте с определенным id
DELETE_STUDENT_SQL = """
DELETE FROM student
WHERE id = 5;
"""


# Задание 5. Выборка студентов из группы 1994
SELECT_GROUP_SQL = """
SELECT
    id,
    fam,
    name,
    year_b,
    gr
FROM student
WHERE gr = 1994
ORDER BY fam, name;
"""


# Задание 6. Поиск студентов групп с шифром специальности, начинающимся на 09
SELECT_SPECIALTY_SQL = """
SELECT
    student.id,
    student.fam,
    student.name,
    student.year_b,
    gruppa.gr,
    gruppa.sp_code,
    specialty.sp_name
FROM student
JOIN gruppa ON gruppa.gr = student.gr
JOIN specialty ON specialty.sp_code = gruppa.sp_code
WHERE gruppa.sp_code LIKE '09%'
ORDER BY gruppa.gr, student.fam, student.name;
"""


# Задание 7. Подключение к базе данных и получение данных из таблиц
def print_query(cursor, title, sql):
    print(title)
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print()


connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.executescript(CREATE_TABLES_SQL)
cursor.executescript(INSERT_DATA_SQL)
cursor.executescript(UPDATE_STUDENT_SQL)
cursor.executescript(DELETE_STUDENT_SQL)
connection.commit()

print_query(cursor, "Студенты группы 1994:", SELECT_GROUP_SQL)
print_query(cursor, "Студенты со специальностью на 09:", SELECT_SPECIALTY_SQL)

connection.close()

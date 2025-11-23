create database subd;
USE subd;

CREATE TABLE students
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(30) NOT NULL,
    lastname    VARCHAR(30) NOT NULL,
    birthday    DATETIME NULL
);

CREATE TABLE subjects
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(30) NOT NULL,
    hours       SMALLINT NOT NULL
);

CREATE TABLE marks
(
    stud_id     INT,
    subj_id     INT,
    ddate       DATETIME DEFAULT CURRENT_TIMESTAMP, 
    mark        TINYINT CHECK (mark > 1 AND mark <= 5),
    
    -- Определение внешних ключей в конце
    FOREIGN KEY (stud_id) REFERENCES students(id),
    FOREIGN KEY (subj_id) REFERENCES subjects(id)
);

INSERT INTO students (name, lastname, birthday) VALUES
('Иван', 'Бор', '2001-04-13'),
('Владимир', 'Скет', '2002-01-26'),
('Александра', 'Мохова', '2003-08-02'),
('Елена', 'Гром', '2004-06-17'),
('Никита', 'Ковриков', '2005-12-10'),
('Анна', 'Штык', '2007-11-15'),
('Матвей', 'Зуев', '2005-08-10'),
('Ольга', 'Кортенко', '2002-01-18'),
('Николай', 'Клоп', '2000-04-12'),
('Евгения', 'Онегина', '2001-06-28');

INSERT INTO subjects (name, hours) VALUES
('Математика', 7),
('Физика', 8),
('Информатика', 11),
('История', 12),
('Литература', 6),
('Химия', 8),
('Биология', 3),
('География', 9),
('Английский', 5),
('Физкультура', 6);

INSERT INTO marks (stud_id, subj_id, mark, ddate) VALUES
(1, 1, 5, '2024-10-20'),   
(2, 2, 4, '2024-10-21'),   
(3, 3, 5, '2024-10-20'), 
(4, 4, 3, '2024-10-22'), 
(5, 5, 4, '2024-10-23'),  
(6, 6, 5, '2024-10-21'), 
(7, 7, 3, '2024-10-22'),
(8, 8, 4, '2024-10-24'),
(9, 9, 5, '2024-10-20'), 
(10, 10, 5, '2024-10-23'); 

INSERT INTO marks (stud_id, subj_id, mark, ddate) VALUES
(1, 2, 4, '2024-10-20'),   
(2, 3, 5, '2024-10-21'),  
(3, 4, 3, '2024-10-20'), 
(4, 5, 4, '2024-10-22'),   
(5, 6, 5, '2024-10-23'), 
(6, 7, 3, '2024-10-21'),
(7, 8, 4, '2024-10-22'), 
(8, 9, 5, '2024-10-24'), 
(9, 10, 3, '2024-10-20'),
(10, 1, 3, '2024-10-23'); 

INSERT INTO marks (stud_id, subj_id, mark, ddate) VALUES
(1, 6, 4, '2024-10-20'),   
(2, 7, 5, '2024-10-21'),   
(3, 8, 5, '2024-10-20'),   
(4, 9, 4, '2024-10-22'),   
(5, 10, 5, '2024-10-23'),  
(6, 1, 4, '2024-10-21'),   
(7, 2, 4, '2024-10-22'),   
(8, 3, 3, '2024-10-24'),   
(9, 4, 4, '2024-10-20'),   
(10, 5, 3, '2024-10-23'); 
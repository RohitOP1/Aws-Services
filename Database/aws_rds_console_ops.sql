create database TestDB;

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT CHECK (age > 0),
    email VARCHAR(100) UNIQUE,
    enrollment_date DATE DEFAULT CURRENT_DATE
);

INSERT INTO students (first_name, last_name, age, email, enrollment_date)
VALUES
('John', 'Doe', 20, 'john.doe@example.com', '2023-01-15'),
('Jane', 'Smith', 22, 'jane.smith@example.com', '2023-02-10'),
('Mark', 'Taylor', 19, 'mark.taylor@example.com', '2023-03-05'),
('Emily', 'Brown', 21, 'emily.brown@example.com', '2023-04-12'),
('Michael', 'Davis', 23, 'michael.davis@example.com', '2023-05-20'),
('Sarah', 'Miller', 22, 'sarah.miller@example.com', '2023-06-22'),
('David', 'Wilson', 18, 'david.wilson@example.com', '2023-07-17'),
('Sophia', 'Moore', 21, 'sophia.moore@example.com', '2023-08-02'),
('Daniel', 'Taylor', 24, 'daniel.taylor@example.com', '2023-09-18'),
('Olivia', 'Anderson', 19, 'olivia.anderson@example.com', '2023-10-25'),
('William', 'Thomas', 20, 'william.thomas@example.com', '2023-11-07'),
('Ava', 'Jackson', 22, 'ava.jackson@example.com', '2023-12-03'),
('James', 'White', 23, 'james.white@example.com', '2024-01-10'),
('Isabella', 'Harris', 21, 'isabella.harris@example.com', '2024-02-14'),
('Ethan', 'Martin', 20, 'ethan.martin@example.com', '2024-03-06'),
('Mia', 'Garcia', 22, 'mia.garcia@example.com', '2024-04-01'),
('Alexander', 'Rodriguez', 19, 'alexander.rodriguez@example.com', '2024-05-10'),

SELECT * FROM students LIMIT 10;

SELECT first_name, last_name, age FROM students;

SELECT * FROM students WHERE student_id = 1;

UPDATE students
SET age = 21
WHERE student_id = 1;

DELETE FROM students WHERE student_id = 4;
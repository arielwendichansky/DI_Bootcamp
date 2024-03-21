-- EXERCISE 1
-- Part I
-- CREATE TABLE customer(
-- 	id SERIAL PRIMARY KEY NOT NULL,
-- 	first_name VARCHAR (50) NOT NULL, 
-- 	last_name VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE customer_profile(
-- 	customer_profile_id SERIAL PRIMARY KEY NOT NULL, 
-- 	isLoggedIn BOOLEAN DEFAULT FALSE,
-- 	customer_id INT,
-- 	CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customer (id)
-- );

-- INSERT INTO customer(first_name, last_name)
-- VALUES ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive')

-- DELETE FROM customer WHERE first_name = 'John' AND last_name = 'Doe'

-- DELETE FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'

-- INSERT INTO customer(first_name, last_name)
-- VALUES ('John', 'Doe'), ('Jerome', 'Lalu')

-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- VALUES (TRUE, (SELECT id FROM customer WHERE first_name = 'John' AND last_name = 'Doe'));

-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- VALUES (TRUE, (SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- UPDATE customer_profile
-- SET isloggedin = False
-- WHERE customer_profile.customer_id = (SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu');

--Display the first_name of LoggedIn customers
-- SELECT customer.id, customer.first_name, customer.last_name, customer_profile.isLoggedIn as Status
-- FROM customer
-- JOIN customer_profile ON customer.id = customer_profile.customer_id
-- WHERE customer_profile.isLoggedIn = TRUE;

-- Display all customers' first_name and isLoggedIn columns, including those without profiles
-- SELECT c.first_name, COALESCE(cp.isLoggedIn, FALSE) AS isLoggedIn
-- FROM customer c
-- LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

--Display the number of customers that are not LoggedIn
-- SELECT COUNT(*) AS num_not_logged_in
-- FROM customer c
-- LEFT JOIN customer_profile cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn IS NULL OR cp.isLoggedIn = FALSE;

--------------------------------------------------------------------------------

-- Part II:	
-- CREATE TABLE book ( 
-- 	book_id SERIAL PRIMARY KEY,
-- 	title VARCHAR(100) NOT NULL, 
-- 	author  VARCHAR(100) NOT NULL
-- );

-- INSERT INTO book (title, author)
-- VALUES ('Alice In Wonderland', 'Lewis Carroll'), ('Harry Potter', 'J.K Rowling'), ('To kill a mockingbird', 'Harper Lee');

-- CREATE TABLE student(
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100) NOT NULL UNIQUE, 
-- 	age INT CHECK (age <= 15) NOT NULL
-- );

-- INSERT INTO student (name, age)
-- VALUES 
-- 	('John',12),
-- 	('Lera',11),
-- 	('Patrick',10),
-- 	('Bob',14);

-- CREATE TABLE library(
-- 	book_fk_id INT,
-- 	student_fk_id INT,
-- 	borrowed_date DATE,
-- 	PRIMARY KEY (book_fk_id, student_fk_id ),
-- 	CONSTRAINT book_fk_id FOREIGN KEY (book_fk_id) REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	CONSTRAINT student_fk_id FOREIGN KEY (student_fk_id) REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE
--  );
 
 
-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM Student WHERE name = 'John'),
--     '2022-02-15'
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
--     (SELECT student_id FROM Student WHERE name = 'Bob'),
--     '2021-03-03'
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM Student WHERE name = 'Lera'),
--     '2021-05-23'
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES (
--     (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
--     (SELECT student_id FROM Student WHERE name = 'Bob'),
--     '2021-08-12'
-- );

-- Select all columns from the junction table:
-- SELECT * FROM library

-- Select the name of the student and the title of the borrowed books
-- SELECT s.name AS student_name, b.title AS book_title
-- FROM Library l
-- JOIN Student s ON l.student_fk_id = s.student_id
-- JOIN Book b ON l.book_fk_id = b.book_id;

-- Select the average age of the children who borrowed the book "Alice in Wonderland"
-- SELECT AVG(age) AS average_age
-- FROM Student
-- WHERE student_id IN (
--     SELECT student_fk_id
--     FROM Library
--     WHERE book_fk_id = (
--         SELECT book_id
--         FROM Book
--         WHERE title = 'Alice In Wonderland'
--     )
-- );

-- when you delete a student from the Student table,
--all records in the Library table associated with that student (borrowed books) will also be deleted
-- automatically to maintain referential integrity.







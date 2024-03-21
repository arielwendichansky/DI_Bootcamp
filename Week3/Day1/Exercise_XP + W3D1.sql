-- create table students(
-- 	student_id serial primary key,
-- 	last_name varchar(100) not null,
-- 	first_name varchar(50) not null,
-- 	birth_date date not null
--)


-- insert into students (first_name, last_name, birth_date)
-- values
-- ('Marc','Benichou', TO_DATE('02/11/1998', 'DD/MM/YYYY')), 
-- ('Yoan','Cohen', TO_DATE('03/12/2010', 'DD/MM/YYYY'))
-- ('Lea','Benichou', TO_DATE('27/07/1987', 'DD/MM/YYYY')), 
-- ('Amelia','Dux',TO_DATE('07/04/1996', 'DD/MM/YYYY')), 
-- ('David','Grez',TO_DATE('14/06/2003', 'DD/MM/YYYY')), 
-- ('Omer','Simpson',TO_DATE('03/10/1980', 'DD/MM/YYYY'))
-- ('Ariel','Wendichansky',TO_DATE('02/02/1994', 'DD/MM/YYYY')); 
-- select * from students
-- select last_name , first_name from students where student_id = 2
-- select last_name , first_name from students where last_name = 'Benichou' AND first_name = 'Marc'
-- select last_name , first_name from students where last_name = 'Benichou' or first_name = 'Marc'
-- select last_name , first_name from students where first_name ilike '%A%'
-- select last_name , first_name from students where first_name ilike 'A%'
-- select last_name , first_name from students where first_name ilike '%A'
-- select last_name , first_name from students where substring(first_name from length(first_name) - 1 for  1) ilike 'a'
-- select last_name , first_name from students where student_id = 1 or student_id = 3
-- select last_name , first_name from students where birth_date >= '1/01/2000'



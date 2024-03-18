-- select last_name , first_name, birth_dates from students order by last_name asc limit 4;
-- select last_name , first_name, birth_dates from students order by birth_date desc limit 1 ;
select last_name , first_name, birth_date from students order by birth_date desc LIMIT 3 OFFSET 2;

-- select last_name , first_name, birth_dates from students where student_id = 1 or student_id = 3
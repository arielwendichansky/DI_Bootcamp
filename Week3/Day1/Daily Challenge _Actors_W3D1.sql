-- create table actors(
-- actor_id serial primary key,
-- first_name varchar (50) not null,
-- last_name varchar (100) not null,
-- age date not null,
-- number_oscar smallint not null
-- )

-- select * from actors where number_oscar > 3
-- insert into actors (first_name, last_name, age, number_oscar)
-- values ('Adam', 'Sandler','09/09/1966', 0); 

-- select * from actors where last_name ilike 'D%'
-- select * from actors order by last_name asc
-- update actors set age = '1970-01-01' where first_name = 'Matt'

-- delete from actors where actor_id	= 2 returning * 
-- returning shows me what I've deleted or changed
-- alter table actors rename column number_oscar to oscars
-- alter table actors drop column age
-- alter table actors add column birthday date;
-- UPDATE actors SET birthday='1970-01-01' WHERE first_name='Matt' AND last_name='Damon'
-- UPDATE actors SET first_name='Maty' WHERE first_name='Matt' AND last_name='Damon'
-- UPDATE actors SET oscars= 4 WHERE first_name='George' AND last_name='Clooney' returning*
-- delete from actors where first_name = 'Julia' returning *
-- select count(distinct last_name) from actors 
insert into actors (first_name)
values('')
-- the outcome is an error as values can not be null by default.

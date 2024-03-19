-- Exercise 1
-- STEP 1
-- SELECT name FROM language

--STEP 2
-- SELECT film.title, film.description, language.name
-- FROM film
-- JOIN language
-- ON film.language_id = language.language_id

--STEP 3
-- SELECT film.title, film.description, language.name
-- FROM film
-- RIGHT JOIN language ON film.language_id = language.language_id;

--STEP 4
-- CREATE TABLE new_film(
-- 	id serial primary key,
-- 	name varchar(100)
-- ) 


-- INSERT INTO new_film(name)
-- VALUES 
-- ('The Shawshank Redemption'),
-- ('The Godfather'),
-- ('Inception'),
-- ('Pulp Fiction'),
-- ('The Dark Knight'),
-- ('Forrest Gump'),
-- ('The Matrix'),
-- ('Monster INC.'), 
-- ('Titanic'),
-- ('Jurassic Park');

-- SELECT * FROM new_film

--STEP 5
-- CREATE TABLE customer_review(
-- 	review_id serial PRIMARY KEY NOT NULL,
-- 	film_id INTEGER NOT NULL,
-- 	language_id INTEGER NOT NULL,
-- 	title VARCHAR(50),
-- 	score INT CHECK (score BETWEEN 1 AND 10),
-- 	review_text TEXT,
-- 	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- 	FOREIGN KEY (film_id) REFERENCES new_film (id) ON DELETE CASCADE,
-- 	FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE CASCADE
-- );

--STEP 6
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (1, 1, 'Great Movie!', 9, 'The Shawshank Redemption is a masterpiece.'),
-- (2, 1, 'Classic Film', 10, 'The Godfather is an epic crime drama.')

--STEP 7
-- DELETE FROM new_film WHERE name = 'The Shawshank Redemption' 


-- Exercise 2
--STEP 1
-- UPDATE customer_review SET language_id = '2' WHERE film_id = '2'

--STEP 2
-- In the customer table we have as a FK 'Customer Adress'. 
-- it affects the way you insert data into that table because you need to ensure that the values you insert
-- into the foreign key column exist in the referenced table.

--STEP 3
-- DROP TABLE customer_review
-- Dropping a table is a straightforward operation in SQL, but it's irreversible and can lead to data loss if not done carefully.

--STEP 4
-- SELECT COUNT(*) AS outstanding_rentals
-- FROM rental
-- WHERE return_date IS NULL;

--STEP 5
-- SELECT inventory.inventory_id, inventory.film_id, film.title, film.replacement_cost
-- FROM film
-- JOIN inventory ON inventory.film_id = film.film_id 
-- WHERE inventory.inventory_id IN (SELECT rental.inventory_id FROM rental WHERE return_date IS NULL) ORDER BY replacement_cost DESC
-- LIMIT 30;

--STEP 6

-- SELECT film.title, film.film_id, film.description, film_actor.actor_id
-- FROM film 
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE FILM.description ILIKE '%sumo%' AND (actor.first_name ='Penelope' AND actor.last_name = 'Monroe');

-- SELECT film.title, film.film_id, film.description, film.rating, film.length
-- FROM film 
-- WHERE film.length < 60 AND rating = 'R' ORDER BY length ASC;

-- SELECT film.title, film.film_id, film.description
-- FROM film 
-- JOIN inventory ON film.film_id = inventory.film_id
-- JOIN rental ON inventory.inventory_id = rental.inventory_id
-- JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE film.rental_rate > '4.00'
-- AND rental.return_date BETWEEN '2005-07-28 00:00:00' AND '2005-08-01 23:59:59'
-- AND customer.first_name ='Matthew' AND customer.last_name = 'Mahan';


-- SELECT film.title, film.film_id, film.description,film.replacement_cost
-- FROM film 
-- JOIN inventory ON film.film_id = inventory.film_id
-- JOIN rental ON inventory.inventory_id = rental.inventory_id
-- JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE (film.title ILIKE '%boat%' or film.description ILIKE '%boat%')
-- AND (customer.first_name ='Matthew' AND customer.last_name = 'Mahan') order by film.replacement_cost DESC;

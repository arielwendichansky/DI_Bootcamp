-- SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- SELECT DISTINCT create_date FROM customer

-- SELECT * FROM customer ORDER BY first_name desc;
-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
-- SELECT address, phone FROM address WHERE district = 'Texas'
-- SELECT * from film WHERE film_id BETWEEN '15' and '150';
-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'Iron Moon';
-- SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'Mo%';
-- SELECT film_id, title, description, length, rental_rate FROM film ORDER BY rental_rate OFFSET 10 FETCH NEXT 10 ROWS ONLY;
-- SELECT 
-- 	customer.first_name, 
-- 	customer.last_name,
-- 	payment.amount,
-- 	payment.payment_date
-- FROM
-- 	customer
-- JOIN
-- 	payment
-- ON
-- 	customer.customer_id = payment.customer_id
-- ORDER BY payment_id ASC;  
-- SELECT film.title
-- FROM film
-- LEFT JOIN inventory ON film.film_id = inventory.film_id 
-- WHERE inventory.film_id IS NULL;
-- SELECT city.city,country.country
-- FROM city
-- JOIN country ON city.country_id = country.country_id



-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor.
-- Display the actor’s name and the cumulative revenue.

WITH movies_revenue AS(
	SELECT
		c.person_id,
		SUM(m.revenue)  AS actor_revenue
	FROM
		movies.movie m
	RIGHT JOIN
		movies.movie_cast c USING (movie_id)
	GROUP BY
		c.person_id)
		
SELECT
	p.person_name,
	actor_revenue
FROM
	movies_revenue
LEFT JOIN
	movies.person p USING(person_id)
ORDER BY
    2 DESC;
	

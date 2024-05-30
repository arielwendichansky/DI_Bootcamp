
-- 🌟 Task 2: Determine The Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies.
-- Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.
-- Rony's way
WITH tot_avg as(
SELECT avg(vote_average) tot_vote_avg
	FROM movies.movie
),
relevant_movies as (select movie_id
				   from movies.movie
				   WHERE vote_average >= (select tot_vote_avg from tot_avg))
SELECT c.person_id,person_name, count(distinct c.movie_id) as distinct_film 
from movies.movie_cast as c
inner join relevant_movies using (movie_id)
left join movies.person as p using (person_id)
Group by 1,2
order by 3 desc
limit 1

--------------------------------------------------------------------------
-- My way
WITH Avg_Movie_Rating AS(
	SELECT 
		m.movie_id,
		m.title,
		m.release_date,
		m.vote_average,
		AVG(m.vote_average) OVER() AS avg_rating_all_movies
	FROM 
		movies.movie m
)

SELECT 
	p.person_id,
	p.person_name,
	COUNT(movie_id) AS over_avg_actor
FROM
	Avg_Movie_Rating
	LEFT JOIN 
		movies.movie_cast mc USING(movie_id)
	LEFT JOIN 
		movies.person p USING(person_id)
WHERE 
	vote_average > avg_rating_all_movies
GROUP BY
	1,
	2
Order BY
	3 DESC
Limit 1;


-- Task 1: Calculate The Average Budget Growth Rate For Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced.
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.

WITH budget_lag AS (
	SELECT 
		mc.company_id, 
        pc.company_name, 
		MAX(budget) 
			OVER (PARTITION BY mc.company_id ) AS max_budget,
		MIN(budget)
			OVER (PARTITION BY mc.company_id ) AS min_budget
    FROM 
        movies.movie m
    JOIN 
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN 
        movies.production_company pc ON mc.company_id = pc.company_id
)
	SELECT distinct company_id, 
        company_name,    
		(max_budget/ (case when min_budget = 0 then 1 else min_budget end))-1 AS avg_growth
	FROM budget_lag
	Order By 3 DESC;	

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


	
-- 🌟 Task 3: Calculate The Rolling Average Revenue For Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre.
-- Use window functions with the ROWS frame specification to achieve this.


WITH average_revenue_genre AS (
	SELECT
		m.movie_id,
		m.title,
		m.release_date,
		mg.genre_id,
		AVG(m.revenue) OVER(
			PARTITION BY mg.genre_id
			ORDER BY m.release_date DESC
			ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS avg_revenue_last_3
	FROM 
		movies.movie m
	INNER JOIN 
		movies.movie_genres mg USING(movie_id)
)
SELECT 
		genre_id,
		g.genre_name,
		movie_id,
		title,
		release_date,
		avg_revenue_last_3
FROM
		average_revenue_genre
LEFT JOIN
		movies.genre g USING(genre_id)
ORDER BY
		genre_id,
		release_date ;
		
-- 🌟 Task 4: Identify The Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue.
-- Use window functions and CTEs to group movies by their series and calculate the total revenue.

WITH main_character AS(
	SELECT 
		m.movie_id,
		m.title,
		m.revenue,
		mc.character_name,
		mc.cast_order
	FROM 
		movies.movie m
	LEFT JOIN
		movies.movie_cast mc USING(movie_id)
	WHERE 
		mc.cast_order = 0
), 

series_revenue AS (
	SELECT
		character_name,
		sum(revenue) AS total_series_revenue
	FROM 
			main_character
	GROUP BY
			character_name)
SELECT
	character_name,
	total_series_revenue
FROM
	series_revenue
ORDER BY
	2 DESC
LIMIT 1;



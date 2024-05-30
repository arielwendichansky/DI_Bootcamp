		
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


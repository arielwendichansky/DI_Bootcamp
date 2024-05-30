
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

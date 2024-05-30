-- Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each genre.
-- Display the genre name, movie title, budget, and running total budget.

	
WITH run_budget AS(
	SELECT
		mg.genre_id,
		m.title,
		m.budget,
	SUM(m.budget) OVER (PARTITION BY mg.genre_id
				ORDER BY m.release_date ASC
				ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_movie_budget
	FROM
		movies.movie m
	JOIN movies.movie_genres mg USING(movie_id)),
	
total_buget AS (SELECT
	g.genre_name,
	title,
	budget,
	running_movie_budget,
	ROW_NUMBER() OVER(
	PARTITION BY g.genre_name
	ORDER BY running_movie_budget DESC) AS rn
FROM
	run_budget
JOIN
	movies.genre g USING(genre_id))

SELECT
	genre_name,
	MAX(running_movie_budget) AS running_movie_budget
FROM 
	total_buget
WHERE rn=1
GROUP BY
	genre_name
ORDER BY
	running_movie_budget DESC;
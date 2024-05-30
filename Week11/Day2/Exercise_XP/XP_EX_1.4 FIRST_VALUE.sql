-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. 
-- Display the genre name, movie title, and release date.

WITH new_movie AS(
	SELECT
		mg.genre_id,
		m.title,
		m.release_date,
	FIRST_VALUE(m.release_date) OVER (PARTITION BY mg.genre_id
				ORDER BY m.release_date DESC) AS last_movie
	FROM
		movies.movie m
	JOIN movies.movie_genres mg USING(movie_id)),
	
movies_date_ranking AS (
SELECT
	g.genre_name,
	title,
	release_date,
	last_movie,
	ROW_NUMBER() OVER(
	PARTITION BY g.genre_name
	ORDER BY release_date DESC) AS rn
FROM
	new_movie
JOIN
	movies.genre g USING(genre_id))

SELECT
	genre_name,
	title,
	release_date
FROM 
	movies_date_ranking
WHERE rn=1
ORDER BY
	release_date DESC;
-- Use the RANK() function to rank movies by their popularity within each genre.
-- Display the genre name, movie title, and their rank based on popularity.

WITH movie_rank AS(
	SELECT
		m.movie_id,
		m.title,
		m.popularity,
		mg.genre_id,
	RANK() OVER (PARTITION BY genre_id ORDER BY m.popularity DESC) AS movie_ranking
	FROM
		movies.movie m
	JOIN movies.movie_genres mg USING(movie_id))
SELECT 
	g.genre_name,
	title,
	movie_ranking
FROM 
	movie_rank
JOIN
	movies.genre g USING(genre_id)
WHERE 
	movie_ranking = 1;
	


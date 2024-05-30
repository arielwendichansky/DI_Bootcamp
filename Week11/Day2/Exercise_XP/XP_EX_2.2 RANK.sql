WITH Avg_Movie_Rating AS(
	SELECT 
		mc.person_id,
		p.person_name,
		ROUND(AVG(m.vote_average),2) AS avg_rating_director
	FROM 
		movies.movie_crew mc
	LEFT JOIN
		movies.movie m USING(movie_id)
	LEFT JOIN 
		movies.person p USING(person_id)
	WHERE
		mc.job = 'Director'
	GROUP BY
		mc.person_id,
		p.person_name
)

SELECT
	person_name,
	avg_rating_director,
	RANK() OVER (ORDER BY avg_rating_director) AS director_avg_ranking
FROM 
	Avg_Movie_Rating
ORDER BY
	director_avg_ranking DESC
LIMIT 10;


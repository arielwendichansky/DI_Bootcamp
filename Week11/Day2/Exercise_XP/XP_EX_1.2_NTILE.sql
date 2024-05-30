
-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue.
-- Display the company name, movie title, revenue, and quartile.
	
WITH company_quartile AS(
	SELECT
		m.title,
		m.revenue,
		mc.company_id,
	NTILE(10) OVER (PARTITION BY mc.company_id ORDER BY m.revenue DESC) AS quartile
	FROM
		movies.movie m
	JOIN movies.movie_company mc USING(movie_id))
	
SELECT
	pc.company_name,
	title,
	revenue,
	quartile
FROM
	company_quartile
LEFT JOIN
	movies.production_company pc USING(company_id)
WHERE
	quartile IN (1,2,3);

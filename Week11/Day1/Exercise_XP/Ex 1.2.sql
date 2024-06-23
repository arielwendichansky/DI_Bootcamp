-- Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events.
-- Use nested subqueries to filter and aggregate the data.

SELECT 
		nr.region_name,
		COUNT(DISTINCT(gc.id)) AS unique_competitors	
FROM
		olympics.games_competitor AS gc
JOIN 
		olympics.person AS p ON gc.person_id = p.id
JOIN
		olympics.person_region AS pr ON pr.person_id = p.id
JOIN 
		olympics.noc_region AS nr ON pr.region_id = nr.id
WHERE
		gc.id IN (
			SELECT competitor_id
			FROM olympics.competitor_event
			GROUP BY competitor_id
			HAVING COUNT(event_id)>3)
GROUP BY
		nr.region_name
ORDER BY
		unique_competitors DESC LIMIT(5);
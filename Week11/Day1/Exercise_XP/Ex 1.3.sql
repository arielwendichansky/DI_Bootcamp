-- Create a temporary table to store the total number of medals won by each competitor
-- filter to show only those who have won more than 2 medals.
-- Use subqueries to aggregate the data.

CREATE TEMPORARY TABLE medal_counts  (
    person_id INT,
    total_medals INT
);

INSERT INTO medal_counts(person_id, total_medals)
SELECT 
	gc.person_id,
	COUNT(ce.medal_id) AS total_medals
FROM
	olympics.competitor_event AS ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.person p ON gc.person_id = p.id
WHERE 
	ce.medal_id IN ('1','2','3')
GROUP BY
	gc.person_id
HAVING 
	COUNT(ce.medal_id)>2;

SELECT 
	p.full_name,
	medal_counts.total_medals
FROM
	medal_counts 
JOIN
	olympics.person p ON medal_counts.person_id = p.id
ORDER BY
	total_medals DESC;
---------------------------------------------------------------------------------------
SELECT
	p.full_name,
	COUNT(ce.medal_id) AS total_medals
FROM
	olympics.competitor_event AS ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.person p ON gc.person_id = p.id
WHERE ce.medal_id IN ('1','2','3')
GROUP BY
	p.full_name

ORDER BY
	total_medals DESC;
		
	
		
		
	
					

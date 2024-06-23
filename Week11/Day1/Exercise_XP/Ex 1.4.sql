-- Use a subquery within a DELETE statement to remove records of competitors who have not won any medals
-- from a temporary table created for analysis.
DROP TABLE IF EXISTS region_medals;

CREATE TEMPORARY TABLE region_medals(
	region_id INT,
	person_id INT,
	medal_id INT);
	
INSERT INTO region_medals(region_id, person_id, medal_id)
SELECT
	pr.region_id,
	pr.person_id,
	ce.medal_id
FROM
	olympics.competitor_event ce 
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.person_region pr ON gc.person_id = pr.person_id;
---
DELETE FROM
	region_medals rm
WHERE
	rm.medal_id = 4;
---
SELECT 
	nr.region_name,
	COUNT(rm.medal_id) AS won_medals
FROM
	region_medals rm
JOIN
	olympics.noc_region nr ON rm.region_id = nr.id
GROUP BY
	nr.region_name
ORDER BY
	won_medals DESC;

	





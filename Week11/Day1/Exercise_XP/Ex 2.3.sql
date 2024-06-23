--  Identify regions where the average number of medals won per competitor is greater than the overall average.
--  Use subqueries to calculate and compare averages.

-- 1st step : Subquery to calculate overall average medals per competitor
WITH total_region_medals AS(
	SELECT ROUND(AVG(total_medals),2) AS avg_medals_competitors
	FROM(
		SELECT pr.person_id, COUNT(ce.medal_id) AS total_medals
		FROM olympics.competitor_event ce 
		LEFT JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
		LEFT JOIN olympics.person_region pr ON gc.person_id = pr.person_id
		WHERE
			ce.medal_id IN ('1','2','3')
		GROUP BY
			pr.person_id
		) AS medals_per_person
	),
	
-- 2nd Step: Subquery to calculate average medals per region
region_avg_medals AS(
	SELECT region_id, ROUND(AVG(total_medals),2) AS avg_medals
	FROM(
		SELECT pr.region_id, pr.person_id, COUNT(ce.medal_id) AS total_medals
		FROM olympics.competitor_event ce 
		LEFT JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
		LEFT JOIN olympics.person_region pr ON gc.person_id = pr.person_id
		WHERE
			ce.medal_id IN ('1','2','3')
		GROUP BY
			pr.region_id, pr.person_id
		)AS region_medal_per_person
	GROUP BY region_id
)
-- 3rd: Final query to identify regions where avg_medals > overall average
SELECT nr.region_name, ram.avg_medals
FROM region_avg_medals ram
LEFT JOIN olympics.noc_region nr ON ram.region_id = nr.id
WHERE
	ram.avg_medals > (SELECT avg_medals_competitors FROM total_region_medals)
ORDER BY 
	ram.avg_medals DESC;



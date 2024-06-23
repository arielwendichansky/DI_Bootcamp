-- Find the average age of competitors who have won at least one medal, grouped by the type of medal they won.
-- Use a correlated subquery to achieve this.
SELECT 
	m.medal_name, AVG(gc.age)
FROM 
	olympics.competitor_event AS ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN
	olympics.medal m ON ce.medal_id = m.id
WHERE 
	m.medal_name IN ('Gold', 'Silver', 'Bronze')
GROUP BY
	m.medal_name;
			   			


-- Select * from olympics.games_competitor
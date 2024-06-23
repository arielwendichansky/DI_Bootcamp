-- Update the heights of competitors based on the average height of competitors from the same region.
-- Use a correlated subquery within the UPDATE statement.
DROP TABLE IF EXISTS nation_heights;

CREATE TEMPORARY TABLE nation_heights(region_id INT, region_name VARCHAR (200),average_heights NUMERIC);
INSERT INTO nation_heights(region_id, region_name, average_heights)
SELECT 
	pr.region_id,
	nr.region_name,
	AVG(p.height) AS avg_height
FROM
	olympics.person_region pr
JOIN
	olympics.noc_region nr ON pr.region_id = nr.id
JOIN
	olympics.person p ON pr.person_id = p.id
GROUP BY
	region_id,
	region_name
HAVING
	AVG(p.height) > 0
ORDER BY
	avg_height DESC;



UPDATE olympics.person p
SET height = (
	SELECT nh.average_heights
	FROM nation_heights AS nh
	JOIN(
			SELECT MIN(region_id) as region_id, person_id
			FROM olympics.person_region
			GROUP BY person_id
		) pr ON nh.region_id = pr.region_id
		WHERE pr.person_id = p.id
		LIMIT 1  -- Ensure a single value is returned
			)
WHERE 
	height = 0;
	
SELECT * FROM nation_heights;

-- Insert new records into a temporary table for competitors who participated in more than one event in the same games
-- and list their total number of events participated. Use nested subqueries for filtering.

DROP TABLE IF EXISTS event_participant;

CREATE TEMPORARY TABLE event_participant (person_id INT, games_id INT,  total_events NUMERIC);

INSERT INTO event_participant(person_id, games_id, total_events)
SELECT
	gc.person_id,
	gc.games_id,
	COUNT( DISTINCT ce.event_id) AS total_events
FROM
	olympics.competitor_event ce
JOIN
	olympics.games_competitor gc ON ce.competitor_id = gc.id
WHERE
	gc.person_id IN(
					SELECT
						gc_in.person_id
					FROM
						olympics.games_competitor gc_in
					JOIN
						olympics.competitor_event ce_in ON gc_in.id = ce_in.competitor_id
					GROUP BY
						gc_in.person_id, gc_in.games_id
					HAVING
						COUNT(DISTINCT ce_in.event_id) > 1)
GROUP BY
	gc.person_id,
	gc.games_id
ORDER BY
	total_events DESC;

SELECT 
	p.full_name,
	g.games_name,
	ep.total_events
FROM 
	event_participant ep
JOIN
	olympics.games g ON g.id = ep.games_id
JOIN
	olympics.person p ON p.id = ep.person_id;



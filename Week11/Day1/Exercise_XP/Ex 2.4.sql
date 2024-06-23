-- Create a temporary table to track competitors’ participation across different seasons
-- and identify those who have participated in both Summer and Winter games.

DROP TABLE IF EXISTS com_participation;

CREATE TEMPORARY TABLE com_participation(person_id INT, participated_games BOOLEAN);

INSERT INTO com_participation(person_id, participated_games)
-- 1st identifying competitors in more than one game per season 
SELECT
	p.id AS person_id,
	CASE
		WHEN EXISTS(
			SELECT 1
			FROM olympics.games_competitor gc_1
			JOIN olympics.games g_1 ON gc_1.games_id = g_1.id
			WHERE gc_1.person_id = p.id AND g_1.season = 'Summer'
		) AND EXISTS(
			SELECT 1
			FROM olympics.games_competitor gc_2
			JOIN olympics.games g_2 ON gc_2.games_id = g_2.id
			WHERE gc_2.person_id = p.id AND g_2.season = 'Winter'
		)
		THEN TRUE
		ELSE FALSE
	END AS participated_games
FROM olympics.person p;

SELECT p.full_name
FROM olympics.person p
JOIN com_participation cp ON cp.person_id = p.id
WHERE participated_games = TRUE;

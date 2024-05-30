-- Use a CTE and a window function to find the director whose movies have the highest total budget.
-- Display the director’s name and the total budget.

WITH director_budgets AS (
    SELECT
        mc.person_id,
        p.person_name,
        SUM(m.budget) OVER (PARTITION BY mc.person_id) AS total_budget
    FROM
        movies.movie_crew mc
    JOIN
        movies.movie m ON mc.movie_id = m.movie_id
    JOIN
        movies.person p ON mc.person_id = p.person_id
    WHERE
        mc.job = 'Director'
)

SELECT
    person_name,
    total_budget
FROM (
    SELECT
        person_name,
        total_budget,
        RANK() OVER (ORDER BY total_budget DESC) AS budget_rank
    FROM
        director_budgets
) ranked_directors
WHERE
    budget_rank = 1;

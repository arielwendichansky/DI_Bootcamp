-- Task 1: Calculate The Average Budget Growth Rate For Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced.
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.

WITH budget_lag AS (
	SELECT 
		mc.company_id, 
        pc.company_name, 
		MAX(budget) 
			OVER (PARTITION BY mc.company_id ) AS max_budget,
		MIN(budget)
			OVER (PARTITION BY mc.company_id ) AS min_budget
    FROM 
        movies.movie m
    JOIN 
        movies.movie_company mc ON m.movie_id = mc.movie_id
    JOIN 
        movies.production_company pc ON mc.company_id = pc.company_id
)
	SELECT distinct company_id, 
        company_name,    
		(max_budget/ (case when min_budget = 0 then 1 else min_budget end))-1 AS avg_growth
	FROM budget_lag
	Order By 3 DESC;	


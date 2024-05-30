-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in.
-- Display the actor’s name and their rank.
		
WITH movie_counts AS (
    SELECT 
        mc.person_id,
        COUNT(mc.movie_id) AS movie_count
    FROM 
        movies.movie_cast mc
    GROUP BY 
        mc.person_id
),
ranked_actors AS (
    SELECT
        mc.person_id,
        mc.movie_count,
        p.person_name,
        DENSE_RANK() OVER (ORDER BY mc.movie_count DESC) AS actor_rank
    FROM 
        movie_counts mc
    JOIN 
        movies.person p ON mc.person_id = p.person_id
)

SELECT
    person_name,
    movie_count,
    actor_rank
FROM 
    ranked_actors
ORDER BY 
    actor_rank;


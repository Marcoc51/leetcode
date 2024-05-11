SELECT results
FROM (
    SELECT TOP 1 u.name AS results
    FROM Users AS u
    INNER JOIN MovieRating AS mr
    ON u.user_id = mr.user_id
    GROUP BY u.name
    ORDER BY COUNT(mr.movie_id) DESC, 1
) AS user_result
UNION ALL
SELECT results
FROM (
    SELECT TOP 1 m.title AS results
    FROM Movies AS m
    INNER JOIN MovieRating AS mr
    ON m.movie_id = mr.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.title
    ORDER BY AVG(mr.rating * 1.0) DESC, 1
) AS movie_result

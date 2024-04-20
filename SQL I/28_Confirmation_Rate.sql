WITH count_cte AS (
    SELECT c.user_id, COUNT(c.user_id) AS total_count
    FROM Confirmations AS c
    GROUP BY c.user_id
)

SELECT s.user_id, 
ROUND(ISNULL(COUNT(c.action) * 1.0 / MIN(co.total_count), 0), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
AND c.action = 'confirmed'
LEFT JOIN count_cte AS co
ON s.user_id = co.user_id
GROUP BY s.user_id;

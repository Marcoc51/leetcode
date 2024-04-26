WITH Activity_cte AS
(
    SELECT player_id
          ,MIN(event_date) AS event_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(
    COUNT(DISTINCT a1.player_id) * 1.0 / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2
) AS fraction
FROM Activity_cte AS a1
INNER JOIN Activity AS a2
ON a1.player_id = a2.player_id
AND DATEDIFF(DAY,a1.event_date,a2.event_date) = 1;

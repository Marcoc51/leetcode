WITH end_cte AS (
  SELECT machine_id, process_id, activity_type, timestamp
  FROM Activity
  WHERE activity_type = 'end'
)
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity AS a1
INNER JOIN end_cte AS a2
ON a1.machine_id = a2.machine_id
AND a1.process_id = a2.process_id
WHERE a1.activity_type = 'start'
GROUP BY a1.machine_id;

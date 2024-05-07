WITH weight_cte AS (
    SELECT turn
      ,person_id
      ,person_name
      ,weight
      ,SUM(weight) OVER (ORDER BY turn) AS TotalWeight
    FROM Queue
)
SELECT TOP 1 person_name
FROM weight_cte
WHERE TotalWeight <= 1000
ORDER BY TotalWeight DESC

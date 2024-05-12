SELECT visited_on
      ,SUM(amount) AS amount
      ,ROUND(SUM(amount) * 1.0 / 7, 2) AS average_amount
FROM (
    SELECT visited_on
          ,SUM(amount) OVER 
          (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
    FROM (
        SELECT visited_on, SUM(amount) AS amount
        FROM Customer
        GROUP BY visited_on
    ) AS totals) AS result
WHERE DATEADD(DAY, -6, visited_on) IN (SELECT visited_on FROM Customer)
GROUP BY visited_on
ORDER BY visited_on;

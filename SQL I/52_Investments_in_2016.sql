WITH ins_cte AS (
    SELECT pid, tiv_2015, tiv_2016, lat, lon
          ,RANK() OVER(ORDER BY tiv_2015) AS tiv
          ,RANK() OVER(ORDER BY lat, lon) AS loc
    FROM Insurance
)
SELECT ROUND(SUM(tiv_2016 * 1.0), 2) AS tiv_2016
FROM ins_cte
WHERE tiv IN (
    SELECT tiv
    FROM ins_cte
    GROUP BY tiv
    HAVING COUNT(tiv) > 1
)
AND loc NOT IN (
    SELECT loc
    FROM ins_cte
    GROUP BY loc
    HAVING COUNT(loc) > 1
)

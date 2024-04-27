SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales AS s
INNER JOIN (
    SELECT s.product_id, MIN(s.year) AS first_year
    FROM Sales AS s
    GROUP BY s.product_id
) AS s_cte
ON s.product_id = s_cte.product_id
AND s.year = s_cte.first_year;

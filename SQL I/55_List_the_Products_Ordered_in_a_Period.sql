SELECT p.product_name, SUM(o.unit) AS unit
FROM Products AS p
LEFT JOIN Orders AS o
ON p.product_id = o.product_id
WHERE LEFT(o.order_date, 7) = '2020-02'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;

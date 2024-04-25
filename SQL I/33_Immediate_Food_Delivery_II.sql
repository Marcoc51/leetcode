WITH Delivery_cte AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS order_id
    FROM Delivery
)

SELECT ROUND(SUM(CASE
        WHEN order_date = customer_pref_delivery_date THEN 1
        ELSE 0
       END) * 100.0 / COUNT(DISTINCT customer_id), 2) AS immediate_percentage
FROM Delivery_cte
WHERE order_id = 1;

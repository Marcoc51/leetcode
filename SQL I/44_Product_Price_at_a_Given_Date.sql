WITH Price AS (
    SELECT product_id, first_value(new_price) OVER(PARTITION BY product_id ORDER BY change_date DESC) AS price
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT p.product_id, ISNULL(MIN(pr.price), 10) AS price
FROM Products As p
LEFT JOIN Price AS pr
ON p.product_id = pr.product_id
Group BY p.product_id;

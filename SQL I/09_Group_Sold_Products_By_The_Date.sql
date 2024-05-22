-- MySQL Solution
SELECT sell_date
      ,COUNT(DISTINCT product) AS num_sold
      ,GROUP_CONCAT(DISTINCT product SEPARATOR ',') as products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;

-- SQL Server Solution
SELECT sell_date
      ,COUNT(product) AS num_sold
      ,STRING_AGG(product, ',') WITHIN GROUP (ORDER BY product) AS products
FROM (SELECT DISTINCT sell_date, product FROM Activities) AS a
GROUP BY sell_date
ORDER BY sell_date;

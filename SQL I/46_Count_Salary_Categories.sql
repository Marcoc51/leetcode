WITH salary_cte AS (
    SELECT account_id
          ,income
          ,CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
            ELSE 'High Salary'
           END AS category
    FROM Accounts
)
SELECT c.category, COUNT(s.category) AS accounts_count
FROM salary_cte AS s
RIGHT JOIN (VALUES('Low Salary'),('High Salary'),('Average Salary')) AS c(category)
ON s.category = c.category
GROUP BY c.category;

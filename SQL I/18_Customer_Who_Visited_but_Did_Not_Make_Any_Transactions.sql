-- First Solution
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id

-- Second Solution
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
WHERE v.visit_id NOT IN (SELECT DISTINCT visit_id FROM Transactions)
GROUP BY v.customer_id

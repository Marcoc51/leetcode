DELETE P1
FROM Person P1
JOIN (
  SELECT MIN(id) AS min_id, email
  FROM Person
  GROUP BY email
) P2
ON P1.id > P2.min_id
AND P1.email = P2.email;

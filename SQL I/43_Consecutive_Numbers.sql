SELECT l.num AS ConsecutiveNums
FROM Logs AS l
INNER JOIN Logs AS l1
ON l.num = l1.num
AND l1.id = l.id + 1
INNER JOIN Logs AS l2
ON l.num = l2.num
AND l2.id = l.id + 2
GROUP BY l.num;

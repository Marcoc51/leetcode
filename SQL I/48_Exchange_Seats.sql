SELECT s1.id, ISNULL(s2.student, s1.student) AS student
FROM Seat AS s1
LEFT JOIN Seat AS s2
ON s1.id + 1 = s2.id
WHERE s1.id % 2 = 1
UNION
SELECT s1.id, s2.student AS student
FROM Seat AS s1
LEFT JOIN Seat AS s2
ON s1.id - 1 = s2.id
WHERE s1.id % 2 = 0
ORDER BY s1.id;

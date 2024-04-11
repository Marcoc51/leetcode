SELECT w2.id AS Id
FROM Weather AS w1
INNER JOIN Weather AS w2
ON DATEDIFF(DAY, w1.recordDate, w2.recordDate) = 1
AND w2.temperature > w1.temperature

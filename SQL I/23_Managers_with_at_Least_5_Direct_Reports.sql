SELECT mng.name
FROM Employee AS emp
INNER JOIN Employee AS mng
ON emp.managerId = mng.id
GROUP BY mng.id, mng.name
HAVING COUNT(mng.id) >= 5;

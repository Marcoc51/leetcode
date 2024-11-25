SELECT emp.name AS Employee
FROM Employee AS emp
INNER JOIN Employee AS mng
ON emp.managerId = mng.id
WHERE emp.salary > mng.salary;

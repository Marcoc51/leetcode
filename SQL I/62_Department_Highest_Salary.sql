SELECT Department, e.name AS Employee, s.Salary
FROM Employee AS e
INNER JOIN (
    SELECT dep.name AS Department, e.departmentId, MAX(e.salary) AS Salary
    FROM Employee AS e
    INNER JOIN Department AS dep
    ON e.departmentId = dep.id
    GROUP BY dep.name, e.departmentId
) AS s
ON e.departmentId = s.departmentId
AND e.salary = s.Salary;

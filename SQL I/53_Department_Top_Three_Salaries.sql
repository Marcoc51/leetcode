SELECT Department
      ,Employee
      ,Salary
FROM (
    SELECT e.id
          ,e.name AS Employee
          ,e.salary
          ,d.name AS Department
          ,DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary DESC) AS Rank
    FROM Employee AS e
    INNER JOIN Department AS d
    ON e.departmentId = d.id
) AS salary
WHERE Rank IN (1, 2, 3)

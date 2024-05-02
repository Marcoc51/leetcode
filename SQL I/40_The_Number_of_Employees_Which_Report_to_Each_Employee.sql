SELECT m.employee_id
      ,m.name
      ,COUNT(e.employee_id) AS reports_count
      ,ROUND(AVG(e.age * 1.0), 0) AS average_age
FROM Employees AS e
INNER JOIN Employees AS m
ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;

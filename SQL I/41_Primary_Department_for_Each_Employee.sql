WITH deps_count AS
(
    SELECT employee_id, COUNT(department_id) AS dep_count
    FROM Employee
    GROUP BY employee_id
)
SELECT e.employee_id, e.department_id
FROM Employee AS e
INNER JOIN deps_count AS d
ON e.employee_id = d.employee_id
WHERE d.dep_count = 1
OR e.primary_flag = 'Y'

DECLARE @total AS INTEGER = (SELECT COUNT(user_id) FROM Users);

SELECT r.contest_id, ROUND(COUNT(r.user_id) * 100.0 / @total, 2) AS percentage
FROM Register AS r
INNER JOIN Users AS u
ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id;

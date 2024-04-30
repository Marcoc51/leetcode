SELECT MAX(num) AS num
FROM (
    SELECT num, COUNT(num) AS count_num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS nums

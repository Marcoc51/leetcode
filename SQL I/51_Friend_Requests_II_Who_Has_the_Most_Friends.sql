SELECT TOP(1) ISNULL(requester_id, a.accepter_id) AS id
             ,ISNULL(COUNT(accept_date), 0) + ISNULL(MIN(a.num), 0) AS num
FROM RequestAccepted AS r
FULL OUTER JOIN (
    SELECT accepter_id, COUNT(accept_date) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
) AS a
ON r.requester_id = a.accepter_id
GROUP BY ISNULL(requester_id, a.accepter_id)
ORDER BY num DESC;

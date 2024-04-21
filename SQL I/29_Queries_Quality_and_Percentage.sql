SELECT q.query_name, 
       ROUND(AVG(q.rating * 1.0 / q.position), 2) AS quality, 
       ROUND(AVG((CASE 
                    WHEN q.rating < 3 THEN 1
                    ELSE 0
                    END) * 100.0), 2) AS poor_query_percentage
FROM Queries AS q
WHERE q.query_name <> 'null'
GROUP BY q.query_name;

SELECT 
    *
FROM 
    products
WHERE 
    description LIKE '%SN____-____%'
AND 
    description LIKE '%SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]%'
AND 
    PATINDEX('%[^0-9]SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][^0-9]%', description + ' ') > 0
ORDER BY 
    product_id;

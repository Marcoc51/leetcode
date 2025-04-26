SELECT 
    *
FROM 
    Users
WHERE 
    email LIKE '%@%.com'
AND 
    email NOT LIKE '%[^A-Za-z0-9_]%@%'
AND 
    email NOT LIKE '%@%[0-9]%.com%';

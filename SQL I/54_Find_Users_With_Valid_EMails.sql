SELECT user_id, name, mail
FROM Users
WHERE mail LIKE '[a-zA-Z]%@leetcode.com' 
AND mail NOT LIKE '%[^0-9a-zA-Z_.-]%@leetcode.com';

UPDATE Salary
SET sex = (
  CASE
  WHEN sex = 'f' then 'm'
  WHEN sex = 'm' then 'f'
END)
WHERE sex = 'm'
OR sex = 'f';

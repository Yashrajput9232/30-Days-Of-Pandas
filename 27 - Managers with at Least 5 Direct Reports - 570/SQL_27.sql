SELECT 
    e.name
FROM employee e 
JOIN employee e1 ON e.id = e1.managerid
GROUP BY e.id, e.name
HAVING COUNT(*) >= 5;
WITH CTE AS (
    SELECT 
        CASE 
            WHEN salary < (SELECT MAX(DISTINCT salary) FROM Employee) 
            THEN salary 
            ELSE NULL 
        END AS SecondHighestSalary
    FROM Employee
    ORDER BY salary DESC
)

SELECT 
    MAX(SecondHighestSalary) AS SecondHighestSalary 
FROM CTE;

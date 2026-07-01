# Write your MySQL query statement below
WITH RankedSalaries AS (
    SELECT
        departmentId,
        name AS Employee,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as r
    FROM Employee
)
SELECT
    d.name AS Department,
    rs.Employee,
    rs.salary AS Salary

FROM RankedSalaries rs
JOIN Department d ON rs.departmentId = d.id
WHERE rs.r <= 3;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
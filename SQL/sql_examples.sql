-- Using WHERE - filter rows before grouping
SELECT *
FROM Employees
WHERE Department = 'Sales';

-- Using Having - filter groups where employee count > 5
SELECT Department, COUNT(*) AS emp_count
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;

-- Combining WHERE and HAVING
-- WHERE → remove rows with salary ≤ 50,000
-- GROUP BY → group the remaining rows
-- HAVING → keep only groups where total salary > 2,00,000
SELECT Department, SUM(salary) AS total_salary
FROM Employees
WHERE salary > 50000
GROUP BY Department
HAVING SUM(salary) > 200000;

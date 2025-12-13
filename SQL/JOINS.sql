-- ON
-- Example 1: Basic JOIN using ON
-- ON defines how rows are connected (emp_id matches id).
SELECT name, salary
FROM employees e
JOIN salaries s
ON e.emp_id = s.id;

-- Self Join Example (common interview question)
-- e1 → refers to employees table (employee)
-- e2 → refers to employees table (manager)
-- This is possible only using table aliases.
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.id;

-- Using WHERE - filter rows before grouping
SELECT *
FROM Employees
WHERE Department = 'Sales';


-- GROUP BY
-- | id | department | salary |
-- | -- | ---------- | ------ |
-- | 1  | HR         | 30000  |
-- | 2  | IT         | 50000  |
-- | 3  | HR         | 35000  |
-- | 4  | IT         | 60000  |

-- Example 1: total salary per department
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;
-- Output:
-- | department | total_salary |
-- | ---------- | ------------ |
-- | HR         | 65000        |
-- | IT         | 110000       |

-- Example 2: Count employees per department
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department;

-- Example 3: GROUP BY with multiple columns
-- Count employees per department and role
SELECT department, role, COUNT(*) AS total
FROM employees
GROUP BY department, role;


-- Using HAVING - filter groups where employee count > 5
SELECT Department, COUNT(*) AS emp_count
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;

SELECT product, SUM(amount) AS total_sales
FROM sales
GROUP BY product
HAVING SUM(amount) > 250;

-- COUNT(*)
-- Counts all rows, including those with NULL values
-- Returns total number of rows in the employees table.(ie total employees)
-- | id | bonus |
-- | -- | ----- |
-- | 1  | 1000  |
-- | 2  | NULL  |
-- | 3  | 2000  |

-- Returns 3 (because all rows are counted)
SELECT COUNT(*)
FROM employees;

-- Returns 2 (because NULL bonus is ignored)
SELECT COUNT(bonus) FROM employees;

-- COUNT(column_name)
-- Counts only non-NULL values in the specified column

-- Combining WHERE and HAVING
-- WHERE → remove rows with salary ≤ 50,000
-- GROUP BY → group the remaining rows
-- HAVING → keep only groups where total salary > 2,00,000
SELECT Department, SUM(salary) AS total_salary
FROM Employees
WHERE salary > 50000
GROUP BY Department
HAVING SUM(salary) > 200000;

SELECT department, COUNT(*) AS emp_count
FROM employees
WHERE salary > 30000       -- filters rows before grouping
GROUP BY department
HAVING COUNT(*) > 5;       -- filters groups after grouping

-- Keeps only cities where the average age is < 30.
SELECT city, AVG(age) AS avg_age
FROM customers
GROUP BY city
HAVING AVG(age) < 30;


-- COALESCE

-- Returns the first non-null value from the list
-- Example: returns 10- Because 10 is the first non-NULL value.
SELECT COALESCE(NULL, NULL, 10, 20);

-- Practical Example 1: Replace NULL with Default Value
-- Here, COALESCE returns bonus if present, otherwise 0.
-- | name    | bonus |
-- | ------- | ----- |
-- | Farzana | 5000  |
-- | Anu     | NULL  |
-- | Rahim   | NULL  |

-- Output:
-- | name    | bonus_amount |
-- | ------- | ------------ |
-- | Farzana | 5000         |
-- | Anu     | 0            |
-- | Rahim   | 0            |

SELECT name, COALESCE(bonus, 0) AS bonus_amount
FROM employees;

-- Practical Example 2: Handling NULL in String Concatenation
-- If last_name is NULL → output remains clean, not NULL.
SELECT COALESCE(first_name, '') || ' ' || COALESCE(last_name, '')
FROM users;

-- Practical Example 3: Fallback Values
-- If email is NULL, use phone; if both are NULL, use 'No contact info'.
SELECT COALESCE(email, phone, 'No contact info') AS contact
FROM customers;


### ON clause

*ON* is used in SQL JOINs to specify the join condition — that is, how two tables should be matched.
You use *ON* to connect tables using a condition like:
- matching columns
- inequalities
- multiple conditions
- different column names

#### Syntax
SELECT *
FROM table1
JOIN table2
ON table1.col = table2.col;

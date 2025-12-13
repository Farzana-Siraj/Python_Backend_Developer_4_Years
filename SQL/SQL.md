### INSERT

*INSERT* is used to add new rows into a table (manually or using SELECT).

### Aggregate functions

- COUNT()
- SUM()
- AVG()
- MAX()
- MIN()

### GROUP BY

**GROUP BY** is used to *group rows that have the same values* in one or more columns and then apply *aggregate functions* on those groups.

#### Why do we use GROUP BY?

To get summary results like:
- Total salary per department
- Count of employees per role
- Total sales per month
- Average marks per student

### HAVING

**HAVING** is used to filter groups created by *GROUP BY* after aggregation.
It works like *WHERE*, but *WHERE cannot be used with aggregate functions*, whereas HAVING can.

#### Why do we use HAVING?

- To filter results after grouping
- To apply conditions on aggregate values

### Difference between *WHERE* clause and *HAVING* clause?

WHERE filters rows before grouping, while HAVING filters groups after aggregation. WHERE cannot be used with aggregate functions, but HAVING can.
- **WHERE** filters raw data row by row before any grouping happens.
- **HAVING** filters groups created by *GROUP BY*, usually using aggregate functions.

| Feature                            | WHERE                                                        | HAVING                              |
| ---------------------------------- | ------------------------------------------------------------ | ----------------------------------- |
| **When it is applied**             | Before grouping (on individua rows)                         | After grouping (on aggregated data) |
| **Used with**                      | SELECT, UPDATE, DELETE                                       | SELECT (with GROUP BY)              |
| **Can filter aggregated results?** | ❌ Cannot be used with aggregate functions (SUM, COUNT, AVG…) | ✅ Can filter aggregated results     |
| **Purpose**                        | Filter rows *before* grouping                                | Filter groups *after* aggregation   |
| **Execution Order**                | Applied first                                                | Applied after WHERE and GROUP BY    |

### count(*)

**COUNT(*)** is an aggregate function that counts all rows in a table — including rows that contain NULL values.

#### COUNT(*) vs COUNT(column_name)

| Function          | What it counts                                    |
| ----------------- | ------------------------------------------------- |
| **COUNT(*)**      | Counts **all rows** (null or non-null)            |
| **COUNT(column)** | Counts only rows where the **column is NOT NULL** |


### COALESCE()

**COALESCE()** is a SQL function that returns the first *non-NULL* value from a list of arguments(or expressions) and is commonly used to replace *NULL* values or provide fallback values.
It checks values from left to right, and the moment it finds a non-NULL value, it returns it.

#### Why is COALESCE used?

- To replace NULL values with a default value
- To handle optional fields
- To avoid NULL results in calculations
- To prevent NULL values from breaking string concatenation


### UNION

**UNION** is used to combine results from two SELECT queries and remove duplicate rows.
**Syntax:**
SELECT column1, column2 FROM table1
UNION
SELECT column1, column2 FROM table2;

**Rules:**

- Both queries must return same number of columns
- Data types must be compatible

#### UNION ALL

- UNION ALL keeps duplicates (faster)

### MINUS (also called EXCEPT in some SQL systems)

**MINUS** returns rows that exist in the first query but NOT in the second.

**Syntax (Oracle, PostgreSQL uses EXCEPT):**

SELECT column FROM table1
MINUS
SELECT column FROM table2;


### INTERSECT

**INTERSECT** returns only the rows that are common in the results of two SELECT queries. it returns the rows that appear in both SELECT queries, removing duplicates. It is used to find common records between datasets.

**In other words:**
INTERSECT = common rows between two result sets (like logical AND)

**Requirements:**
- Both queries must return the same number of columns
- Data types must be compatible
- Removes duplicate rows

**Syntax**
SELECT column1, column2 FROM table1
INTERSECT
SELECT column1, column2 FROM table2;


### ALIAS

An alias is a temporary name given to a table or column to make SQL queries shorter and easier to read.
Aliases exist only during the query execution — they do NOT change actual table/column names in the database.

#### 1. Column Alias

Used to rename a column in the output.

#### 2. Table Alias

Used to give a short name to a table — very helpful in JOINs.

#### Why use aliases?

- Make queries shorter
- Make JOINs cleaner
- Avoid confusion when column names are same in multiple tables
- Needed in self joins

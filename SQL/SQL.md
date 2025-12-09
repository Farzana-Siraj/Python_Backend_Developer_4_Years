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

**HAVING** is used to filter groups created by GROUP BY after aggregation.
It works like WHERE, but *WHERE cannot be used with aggregate functions*, whereas HAVING can.

#### Why do we use HAVING?

- To filter results after grouping
- To apply conditions on aggregate values

### Difference between *WHERE* clause and *HAVING* clause?

WHERE filters rows before grouping, while HAVING filters groups after aggregation. WHERE cannot be used with aggregate functions, but HAVING can.
- **WHERE** filters raw data row by row before any grouping happens.
- **HAVING** filters groups created by GROUP BY, usually using aggregate functions.

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
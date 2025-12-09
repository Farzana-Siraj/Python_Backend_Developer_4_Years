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

### COALESCE()

**COALESCE()** is a SQL function that returns the first *non-NULL* value from a list of arguments(or expressions) and is commonly used to replace *NULL* values or provide fallback values.
It checks values from left to right, and the moment it finds a non-NULL value, it returns it.

#### Why is COALESCE used?

- To replace NULL values with a default value
- To handle optional fields
- To avoid NULL results in calculations
- To prevent NULL values from breaking string concatenation